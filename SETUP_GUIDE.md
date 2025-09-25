# Discord Affiliate Bot - Complete Setup Guide

## 🎯 What You Have Now

Your Discord Affiliate Bot is now configured with:

### ✅ Base44 Backend Integration
- **App ID**: `68d1f85a602cecfca6c02c10`
- **API Base URL**: `https://base44.app/api/apps/68d1f85a602cecfca6c02c10/functions`
- **Preview URL**: `https://preview--discordaffiliatebot.base44.app`

### ✅ Available Function Endpoints
Your bot can now use these Base44 functions:
- `processDiscordAuth` - Handle Discord OAuth authentication
- `getBotConfig` - Get bot configuration and settings
- `whopWebhook` - Handle Whop payment webhooks
- `generateTrackableLink` - Create trackable affiliate links
- `trackLinkClick` - Track link clicks and conversions
- `updateBotStatus` - Update bot status and health
- `logBotActivity` - Log bot activities and events

### ✅ Discord Bot Configuration
- **Client ID**: `1420475643166068877`
- **Bot Token**: Configured and ready
- **Permissions**: Ready for server integration

## 🚀 Quick Start

### 1. Run Setup
```bash
python setup.py
```

### 2. Start the Bot
```bash
python start_bot.py
```

### 3. Invite Bot to Your Server
Use this URL (replace `YOUR_CLIENT_ID` with `1420475643166068877`):
```
https://discord.com/api/oauth2/authorize?client_id=1420475643166068877&permissions=8&scope=bot%20applications.commands
```

## 🎛️ What Your Bot Can Do

### 1. **Role-Based DM System**
- Automatically send DMs when users get specific roles
- Custom message templates with variables
- Button integration for lead generation

### 2. **Marketing Campaigns**
- Target specific roles with custom messages
- A/B testing for message variants
- Track campaign performance

### 3. **Affiliate Link Tracking**
- Generate trackable affiliate links
- Track clicks and conversions
- Integrate with payment systems (Whop webhooks)

### 4. **Analytics & Logging**
- Log all bot activities
- Track user interactions
- Monitor bot health and status

## 🔧 Configuration Options

### Environment Variables
Your bot uses these environment variables:
- `DISCORD_BOT_TOKEN` - Your Discord bot token
- `API_BASE_URL` - Base44 API endpoint
- `BASE44_APP_ID` - Your Base44 app ID
- `DISCORD_CLIENT_ID` - Discord client ID
- `DISCORD_CLIENT_SECRET` - Discord client secret

### Bot Features
- **Rate Limiting**: Built-in protection against spam
- **Error Handling**: Comprehensive error logging
- **Auto-Refresh**: Updates configuration from Base44
- **Multi-Server**: Works across multiple Discord servers

## 🎯 Next Steps

### 1. **Test Basic Functionality**
- Start the bot and check for errors
- Verify it connects to Discord
- Test role assignment detection

### 2. **Configure Campaigns**
- Set up message templates
- Configure target roles
- Test DM sending

### 3. **Set Up Tracking**
- Configure affiliate links
- Test link generation
- Verify click tracking

### 4. **Deploy to Production**
- Use Docker for deployment
- Set up monitoring
- Configure backup systems

## 🛠️ Development Commands

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run setup
python setup.py

# Start bot
python start_bot.py

# Run with debugging
python -u start_bot.py
```

### Docker Deployment
```bash
# Build image
docker build -t discord-affiliate-bot .

# Run container
docker run -d --env-file .env discord-affiliate-bot
```

## 🔍 Troubleshooting

### Common Issues
1. **Bot won't start**: Check your .env file and Discord token
2. **Permission errors**: Make sure bot has proper Discord permissions
3. **API errors**: Verify Base44 endpoints are accessible
4. **Rate limiting**: Check Discord API rate limits

### Debug Mode
Add this to your .env file for detailed logging:
```
DEBUG=true
LOG_LEVEL=DEBUG
```

## 📊 Monitoring

Your bot automatically:
- Logs all activities to Base44
- Updates status every 5 minutes
- Tracks message delivery success/failure
- Monitors API connectivity

Check your Base44 dashboard at: `https://preview--discordaffiliatebot.base44.app`

## 🎉 You're Ready!

Your Discord Affiliate Bot is now fully configured and ready to:
- Send targeted DMs to users with specific roles
- Run marketing campaigns
- Track affiliate links
- Generate leads and conversions
- Monitor performance through Base44 dashboard

Start with `python setup.py` and then `python start_bot.py` to get running!
