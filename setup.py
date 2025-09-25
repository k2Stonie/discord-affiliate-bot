#!/usr/bin/env python3
"""
Setup script for Discord Affiliate Bot
"""
import os
import shutil

def setup_environment():
    """Set up the environment configuration"""
    print("🔧 Setting up Discord Affiliate Bot...")
    
    # Check if config.env exists
    if os.path.exists('config.env'):
        print("✅ Found config.env file")
        
        # Copy config.env to .env
        try:
            shutil.copy('config.env', '.env')
            print("✅ Created .env file from config.env")
        except Exception as e:
            print(f"❌ Error creating .env file: {e}")
            return False
    else:
        print("❌ config.env file not found!")
        print("Please create config.env with your Discord and Base44 configuration")
        return False
    
    # Check if requirements are installed
    try:
        import discord
        import flask
        import requests
        import aiohttp
        import dotenv
        print("✅ All required packages are installed")
    except ImportError as e:
        print(f"❌ Missing package: {e}")
        print("Please run: pip install -r requirements.txt")
        return False
    
    print("🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Make sure your Discord bot has the required permissions")
    print("2. Run: python start_bot.py")
    print("3. Check the console output for any errors")
    
    return True

if __name__ == '__main__':
    setup_environment()
