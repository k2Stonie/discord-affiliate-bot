#!/usr/bin/env python3
"""
Verification script to test Discord bot token and Base44 API connections
"""
import os
import asyncio
import aiohttp
import discord
from dotenv import load_dotenv

async def test_discord_connection():
    """Test Discord bot token connection"""
    print("🔍 Testing Discord Bot Connection...")
    
    token = os.getenv('DISCORD_BOT_TOKEN')
    if not token:
        print("❌ DISCORD_BOT_TOKEN not found in environment")
        return False
    
    try:
        # Create a simple bot instance to test the token
        intents = discord.Intents.all()
        bot = commands.Bot(command_prefix='!', intents=intents)
        
        @bot.event
        async def on_ready():
            print(f"✅ Discord bot connected successfully!")
            print(f"   Bot Name: {bot.user}")
            print(f"   Bot ID: {bot.user.id}")
            print(f"   Guilds: {len(bot.guilds)}")
            await bot.close()
        
        # Try to connect with the token
        await bot.start(token)
        return True
        
    except discord.LoginFailure:
        print("❌ Invalid Discord bot token")
        return False
    except Exception as e:
        print(f"❌ Discord connection error: {e}")
        return False

async def test_base44_api():
    """Test Base44 API endpoints"""
    print("\n🔍 Testing Base44 API Connection...")
    
    api_url = os.getenv('API_BASE_URL')
    app_id = os.getenv('BASE44_APP_ID')
    
    if not api_url:
        print("❌ API_BASE_URL not found in environment")
        return False
    
    if not app_id:
        print("❌ BASE44_APP_ID not found in environment")
        return False
    
    print(f"   API URL: {api_url}")
    print(f"   App ID: {app_id}")
    
    try:
        async with aiohttp.ClientSession() as session:
            # Test getBotConfig endpoint
            test_url = f"{api_url}/getBotConfig"
            headers = {'Content-Type': 'application/json', 'User-Agent': 'DiscordBot/1.0'}
            
            payload = {
                'bot_id': app_id,
                'bot_token': os.getenv('DISCORD_BOT_TOKEN')
            }
            
            print(f"   Testing endpoint: {test_url}")
            async with session.post(test_url, json=payload, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    print("✅ Base44 API connection successful!")
                    print(f"   Response: {data}")
                    return True
                else:
                    print(f"❌ Base44 API error: HTTP {response.status}")
                    error_text = await response.text()
                    print(f"   Error details: {error_text}")
                    return False
                    
    except Exception as e:
        print(f"❌ Base44 API connection error: {e}")
        return False

def check_environment_variables():
    """Check all required environment variables"""
    print("🔍 Checking Environment Variables...")
    
    required_vars = {
        'DISCORD_BOT_TOKEN': 'Discord bot authentication token',
        'API_BASE_URL': 'Base44 API endpoint URL',
        'BASE44_APP_ID': 'Base44 application ID',
        'DISCORD_CLIENT_ID': 'Discord client ID',
        'DISCORD_CLIENT_SECRET': 'Discord client secret'
    }
    
    all_present = True
    for var, description in required_vars.items():
        value = os.getenv(var)
        if value:
            # Mask sensitive tokens for display
            if 'TOKEN' in var or 'SECRET' in var:
                display_value = f"{value[:10]}...{value[-10:]}" if len(value) > 20 else "***"
            else:
                display_value = value
            print(f"   ✅ {var}: {display_value}")
        else:
            print(f"   ❌ {var}: Missing ({description})")
            all_present = False
    
    return all_present

async def main():
    """Main verification function"""
    print("🚀 Discord Affiliate Bot - Setup Verification")
    print("=" * 60)
    
    # Load environment variables
    load_dotenv()
    
    # Check environment variables
    env_ok = check_environment_variables()
    
    if not env_ok:
        print("\n❌ Environment setup incomplete. Please check your .env file.")
        return
    
    print("\n" + "=" * 60)
    
    # Test Discord connection
    discord_ok = await test_discord_connection()
    
    # Test Base44 API
    base44_ok = await test_base44_api()
    
    print("\n" + "=" * 60)
    print("📊 VERIFICATION SUMMARY:")
    print(f"   Environment Variables: {'✅ OK' if env_ok else '❌ FAILED'}")
    print(f"   Discord Connection: {'✅ OK' if discord_ok else '❌ FAILED'}")
    print(f"   Base44 API: {'✅ OK' if base44_ok else '❌ FAILED'}")
    
    if env_ok and discord_ok and base44_ok:
        print("\n🎉 ALL TESTS PASSED! Your bot is ready to use.")
        print("\nNext steps:")
        print("1. Invite your bot to a Discord server")
        print("2. Configure campaigns in Base44 dashboard")
        print("3. Start your bot with: python start_bot.py")
    else:
        print("\n❌ Some tests failed. Please fix the issues above.")
    
    print("\n" + "=" * 60)

if __name__ == '__main__':
    # Import discord commands here to avoid import issues
    from discord.ext import commands
    asyncio.run(main())
