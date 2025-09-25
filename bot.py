#!/usr/bin/env python3
import discord
from discord.ext import commands
import asyncio
import aiohttp
import os
import time
import urllib.parse
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
BOT_ID = os.getenv('BASE44_APP_ID', '68d1f85a602cecfca6c02c10')
API_BASE_URL = os.getenv('API_BASE_URL', 'https://base44.app/api/apps/68d1f85a602cecfca6c02c10/functions')

if not DISCORD_BOT_TOKEN:
    print(' Error: DISCORD_BOT_TOKEN environment variable is required!')
    exit(1)

intents = discord.Intents.all()
discord_bot = commands.Bot(command_prefix='!', intents=intents)

class Base44Client:
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url
        self.session = None
    
    async def call_function(self, function_name, payload=None):
        try:
            if not self.session:
                self.session = aiohttp.ClientSession()
            url = f'{self.api_base_url}/functions/{function_name}'
            headers = {'Content-Type': 'application/json', 'User-Agent': 'DiscordBot/1.0'}
            async with self.session.post(url, json=payload or {}, headers=headers) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f' API call failed: {function_name} - Status: {response.status}')
                    return None
        except Exception as e:
            print(f' Error calling {function_name}: {e}')
            return None
    
    async def get_bot_config(self, bot_id, bot_token):
        payload = {'bot_id': bot_id, 'bot_token': bot_token}
        return await self.call_function('getBotConfig', payload)
    
    async def log_bot_activity(self, activity_data):
        return await self.call_function('logBotActivity', activity_data)
    
    async def update_bot_status(self, status_data):
        return await self.call_function('updateBotStatus', status_data)
    
    async def close(self):
        if self.session:
            await self.session.close()

class BotRateLimiter:
    def __init__(self):
        self.last_dm_time = {}
        self.rate_limit_delay = 1.0
    
    async def send_dm_safely(self, user, content, buttons=None):
        try:
            user_id = str(user.id)
            current_time = time.time()
            if user_id in self.last_dm_time:
                time_since_last = current_time - self.last_dm_time[user_id]
                if time_since_last < self.rate_limit_delay:
                    await asyncio.sleep(self.rate_limit_delay - time_since_last)
            self.last_dm_time[user_id] = time.time()
            if buttons:
                view = create_button_view(buttons)
                await user.send(content, view=view)
            else:
                await user.send(content)
            return True, None
        except discord.Forbidden:
            return False, 'User has DMs disabled'
        except discord.HTTPException as e:
            return False, f'HTTP Error: {str(e)}'
        except Exception as e:
            return False, f'Unknown error: {str(e)}'

class AffiliateBot:
    def __init__(self, bot_token, api_base_url, bot_id):
        self.bot_token = bot_token
        self.api_base_url = api_base_url
        self.bot_id = bot_id
        self.rate_limiter = BotRateLimiter()
        self.base44_client = Base44Client(api_base_url)
        self.current_config = None
        
    async def get_bot_config(self):
        try:
            config = await self.base44_client.get_bot_config(self.bot_id, self.bot_token)
            if config and config.get('success'):
                self.current_config = config.get('data', {})
                return self.current_config
            else:
                print(' Failed to get bot config from Base44 platform - using default config')
                # Return a default configuration if Base44 is not available
                self.current_config = {
                    'active': True,
                    'affiliate_id': 'default_affiliate',
                    'message_templates': [],
                    'target_roles': [],
                    'affiliate_links': []
                }
                return self.current_config
        except Exception as e:
            print(f' Error getting bot config: {e} - using default config')
            # Return a default configuration if there's an error
            self.current_config = {
                'active': True,
                'affiliate_id': 'default_affiliate',
                'message_templates': [],
                'target_roles': [],
                'affiliate_links': []
            }
            return self.current_config
    
    async def log_bot_activity(self, activity_type, **kwargs):
        try:
            activity_data = {
                'bot_id': self.bot_id,
                'activity_type': activity_type,
                'timestamp': datetime.utcnow().isoformat() + 'Z',
                **kwargs
            }
            result = await self.base44_client.log_bot_activity(activity_data)
            if result and result.get('success'):
                print(f' Logged activity: {activity_type}')
            else:
                print(f' Failed to log activity: {activity_type}')
        except Exception as e:
            print(f' Error logging activity: {e}')
    
    async def update_bot_status(self, status, message=None, stats=None):
        try:
            status_data = {
                'bot_id': self.bot_id,
                'status': status,
                'message': message,
                'stats': stats or {}
            }
            result = await self.base44_client.update_bot_status(status_data)
            if result and result.get('success'):
                print(f' Updated bot status: {status}')
            else:
                print(f' Failed to update status: {status}')
        except Exception as e:
            print(f' Error updating status: {e}')
    
    def process_message_template(self, template, user, affiliate_id):
        content = template['content']
        content = content.replace('{username}', user.display_name)
        content = content.replace('{user_mention}', user.mention)
        content = content.replace('{affiliate_id}', str(affiliate_id))
        content = content.replace('{server_name}', user.guild.name if user.guild else 'Unknown Server')
        return content
    
    async def get_users_by_roles(self, guild, target_roles):
        valid_users = []
        enabled_role_ids = [role['role_id'] for role in target_roles if role['enabled']]
        for member in guild.members:
            if any(str(role.id) in enabled_role_ids for role in member.roles):
                valid_users.append(member)
        return valid_users
    
    def select_message_variant(self, user_id, ab_tests):
        if not ab_tests:
            return None
        user_hash = hash(user_id) % 2
        return 'A' if user_hash == 0 else 'B'
    
    def create_trackable_link(self, original_url, affiliate_id, campaign_id):
        tracking_code = f'{affiliate_id}_{campaign_id}_{int(time.time())}'
        encoded_url = urllib.parse.quote(original_url)
        return f'{self.api_base_url}/functions/trackLinkClick?code={tracking_code}&redirect={encoded_url}'
    
    async def process_campaign(self, template, config):
        try:
            target_users = []
            for guild in discord_bot.guilds:
                users = await self.get_users_by_roles(guild, config.get('target_roles', []))
                target_users.extend(users)
            print(f' Found {len(target_users)} target users')
            for user in target_users:
                try:
                    variant = self.select_message_variant(str(user.id), template.get('ab_tests', []))
                    content = self.process_message_template(template, user, config.get('affiliate_id', 'default'))
                    buttons = None
                    if template.get('has_buttons', False):
                        buttons = []
                        for label in template.get('button_labels', []):
                            link_name = template.get('selected_link_name', 'main_affiliate_link')
                            original_url = next(
                                (link['url_template'] for link in config.get('affiliate_links', []) 
                                 if link['name'] == link_name), 
                                '#'
                            )
                            trackable_url = self.create_trackable_link(
                                original_url, 
                                config.get('affiliate_id', 'default'), 
                                template['name']
                            )
                            buttons.append({
                                'label': label,
                                'url': trackable_url,
                                'style': 'primary'
                            })
                    success, error = await self.rate_limiter.send_dm_safely(user, content, buttons)
                    await self.log_bot_activity('message_sent',
                        user_id=str(user.id),
                        message_sent=content,
                        role_targeted=config.get('target_roles', [{}])[0].get('role_name', 'Unknown') 
                        if config.get('target_roles') else 'Unknown',
                        success=success,
                        error_message=error if not success else None,
                        variant=variant
                    )
                    if success:
                        print(f' Sent DM to {user.display_name}')
                    else:
                        print(f' Failed to send DM to {user.display_name}: {error}')
                except Exception as e:
                    print(f' Error processing user {user.display_name}: {e}')
                    await self.log_bot_activity('error',
                        error_message=str(e),
                        success=False
                    )
        except Exception as e:
            print(f' Error processing campaign: {e}')
            await self.log_bot_activity('error',
                error_message=str(e),
                success=False
            )
    
    async def main_loop(self):
        while True:
            try:
                config = await self.get_bot_config()
                if not config.get('active', False):
                    print(' Bot is paused, waiting...')
                    await asyncio.sleep(60)
                    continue
                print(' Processing bot configuration from Base44 platform...')
                templates = config.get('message_templates', [])
                if templates:
                    for template in templates:
                        await self.process_campaign(template, config)
                    print(f' Processed {len(templates)} message templates')
                else:
                    print(' No message templates configured yet - bot is ready and waiting')
                
                await self.update_bot_status('active', 'Bot running smoothly', {
                    'messages_sent': len(templates),
                    'templates_configured': len(templates)
                })
                print(' Waiting 5 minutes before next cycle...')
                await asyncio.sleep(300)
            except Exception as e:
                print(f' Error in main loop: {e}')
                await self.log_bot_activity('error', error_message=str(e), success=False)
                await asyncio.sleep(60)
    
    async def close(self):
        await self.base44_client.close()

def create_button_view(buttons):
    view = discord.ui.View()
    for button_data in buttons:
        button = discord.ui.Button(
            label=button_data['label'],
            url=button_data['url'],
            style=getattr(discord.ButtonStyle, button_data.get('style', 'primary'))
        )
        view.add_item(button)
    return view

affiliate_bot = AffiliateBot(DISCORD_BOT_TOKEN, API_BASE_URL, BOT_ID)

@discord_bot.event
async def on_ready():
    print(f' Logged in as {discord_bot.user}')
    print(f' Bot is in {len(discord_bot.guilds)} server(s)')
    print(f' Connected to Base44 platform: {API_BASE_URL}')
    for guild in discord_bot.guilds:
        print(f'  - {guild.name} (ID: {guild.id})')
        permissions = guild.me.guild_permissions
        print(f'    Permissions: Send Messages: {permissions.send_messages}, Manage Roles: {permissions.manage_roles}')
    await affiliate_bot.log_bot_activity('startup', success=True)
    await affiliate_bot.update_bot_status('active', 'Bot started successfully')
    asyncio.create_task(affiliate_bot.main_loop())

@discord_bot.event
async def on_member_update(before, after):
    try:
        if len(after.roles) > len(before.roles):
            new_roles = [role for role in after.roles if role not in before.roles]
            for role in new_roles:
                print(f' User {after.display_name} gained role: {role.name}')
                await affiliate_bot.log_bot_activity('user_targeted',
                    user_id=str(after.id),
                    role_targeted=role.name,
                    success=True
                )
    except Exception as e:
        print(f' Error handling member update: {e}')

@discord_bot.event
async def on_error(event, *args, **kwargs):
    print(f' Bot error in {event}: {args}')
    await affiliate_bot.log_bot_activity('error',
        error_message=f'Bot error in {event}: {args}',
        success=False
    )

async def run_bot():
    try:
        await discord_bot.start(DISCORD_BOT_TOKEN)
    except Exception as e:
        print(f' Error starting bot: {e}')
        await affiliate_bot.log_bot_activity('shutdown', success=False)
    finally:
        await affiliate_bot.close()
        await discord_bot.close()

if __name__ == '__main__':
    print(' Starting Base44 Affiliate Bot...')
    print(f' Base44 Platform: {API_BASE_URL}')
    print(f' Bot ID: {BOT_ID}')
    try:
        asyncio.run(run_bot())
    except KeyboardInterrupt:
        print(' Bot stopped by user')
        asyncio.run(affiliate_bot.log_bot_activity('shutdown', success=True))
    except Exception as e:
        print(f' Fatal error: {e}')
        asyncio.run(affiliate_bot.log_bot_activity('shutdown', success=False))
