#!/usr/bin/env python3
"""
Initialize Base44 Bot Configuration
"""
import os
import asyncio
import aiohttp
import json
from dotenv import load_dotenv

async def initialize_bot_config():
    """Initialize the bot configuration in Base44"""
    print("🔧 Initializing Base44 Bot Configuration...")
    
    # Load environment variables
    load_dotenv()
    
    api_url = os.getenv('API_BASE_URL')
    app_id = os.getenv('BASE44_APP_ID')
    bot_token = os.getenv('DISCORD_BOT_TOKEN')
    
    if not all([api_url, app_id, bot_token]):
        print("❌ Missing required environment variables")
        return False
    
    # Create initial bot configuration
    initial_config = {
        "active": True,
        "affiliate_id": "default_affiliate",
        "message_templates": [
            {
                "name": "welcome_message",
                "content": "Welcome {username}! Thanks for joining {server_name}! 🎉\n\nCheck out our latest offers:",
                "has_buttons": True,
                "button_labels": ["Get Started", "Learn More"],
                "selected_link_name": "main_affiliate_link"
            }
        ],
        "target_roles": [
            {
                "role_id": "default",
                "role_name": "New Member",
                "enabled": True
            }
        ],
        "affiliate_links": [
            {
                "name": "main_affiliate_link",
                "url_template": "https://example.com/affiliate",
                "enabled": True
            }
        ],
        "settings": {
            "rate_limit_delay": 1.0,
            "max_dms_per_hour": 100,
            "enable_ab_testing": False
        }
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            # Try to create/update bot config
            config_url = f"{api_url}/getBotConfig"
            headers = {
                'Content-Type': 'application/json',
                'User-Agent': 'DiscordBot/1.0'
            }
            
            payload = {
                'bot_id': app_id,
                'bot_token': bot_token,
                'initial_config': initial_config
            }
            
            print(f"   Sending configuration to: {config_url}")
            async with session.post(config_url, json=payload, headers=headers) as response:
                response_text = await response.text()
                
                if response.status == 200:
                    print("✅ Bot configuration initialized successfully!")
                    data = json.loads(response_text)
                    print(f"   Response: {json.dumps(data, indent=2)}")
                    return True
                elif response.status == 500 and "not found" in response_text:
                    print("⚠️  BotConfig entity not found - this is normal for first setup")
                    print("   The configuration will be created when the bot first runs")
                    return True
                else:
                    print(f"❌ Error initializing config: HTTP {response.status}")
                    print(f"   Response: {response_text}")
                    return False
                    
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

async def test_other_endpoints():
    """Test other Base44 endpoints to see which ones work"""
    print("\n🔍 Testing Other Base44 Endpoints...")
    
    api_url = os.getenv('API_BASE_URL')
    app_id = os.getenv('BASE44_APP_ID')
    
    endpoints_to_test = [
        'logBotActivity',
        'updateBotStatus',
        'generateTrackableLink'
    ]
    
    try:
        async with aiohttp.ClientSession() as session:
            for endpoint in endpoints_to_test:
                test_url = f"{api_url}/{endpoint}"
                headers = {'Content-Type': 'application/json', 'User-Agent': 'DiscordBot/1.0'}
                
                # Simple test payload
                payload = {
                    'bot_id': app_id,
                    'test': True
                }
                
                print(f"   Testing {endpoint}...")
                async with session.post(test_url, json=payload, headers=headers) as response:
                    if response.status == 200:
                        print(f"   ✅ {endpoint}: Working")
                    else:
                        print(f"   ⚠️  {endpoint}: HTTP {response.status}")
                        
    except Exception as e:
        print(f"   ❌ Error testing endpoints: {e}")

async def main():
    """Main function"""
    print("🚀 Base44 Configuration Initialization")
    print("=" * 50)
    
    # Initialize bot config
    config_ok = await initialize_bot_config()
    
    # Test other endpoints
    await test_other_endpoints()
    
    print("\n" + "=" * 50)
    if config_ok:
        print("✅ Configuration setup completed!")
        print("\nNext steps:")
        print("1. Your bot will create the BotConfig when it first runs")
        print("2. Start your bot: python start_bot.py")
        print("3. Configure campaigns via Base44 dashboard")
    else:
        print("❌ Configuration setup failed")
        print("You may need to manually configure your bot in the Base44 dashboard")

if __name__ == '__main__':
    asyncio.run(main())
