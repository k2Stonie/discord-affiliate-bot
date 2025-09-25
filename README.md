# Discord Affiliate Bot

A powerful Discord bot with a web dashboard for managing role-based DMs, marketing campaigns, and lead generation.

## ✨ Features

- **Role DM Management**: Automatically send DMs when users receive specific roles
- **Marketing Campaigns**: Target specific roles with custom messages
- **Get Now Buttons**: Interactive buttons for lead generation
- **Web Dashboard**: Easy-to-use interface for managing all bot functions
- **Custom Templates**: Editable message templates with variable substitution
- **Button Customization**: Custom text, emojis, and colors for buttons
- **Server Logo Integration**: Use custom server logos in DMs
- **Rate Limiting**: Built-in protection against spam
- **Auto-Refresh**: Automatically updates server data when roles/channels change

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Discord bot token
- Discord server with appropriate permissions

### Installation

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd discord-affiliate-bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Discord bot**
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a new application
   - Go to "Bot" section and create a bot
   - Copy the bot token
   - Enable required intents: `Server Members Intent`, `Message Content Intent`

4. **Configure the bot**
   - Open `bot.py`
   - Replace `YOUR_BOT_TOKEN` with your actual bot token (line 15)
   - Save the file

5. **Invite bot to your server**
   - Use this URL (replace `YOUR_BOT_CLIENT_ID` with your bot's Client ID):
   ```
   https://discord.com/api/oauth2/authorize?client_id=YOUR_BOT_CLIENT_ID&permissions=8&scope=bot%20applications.commands
   ```

6. **Run the bot**
   ```bash
   python bot.py
   ```

7. **Access the dashboard**
   - Open your browser and go to: `http://localhost:5000`

## 📋 Bot Commands

- `/sync` - Sync slash commands
- `/test` - Test bot functionality
- `/check` - Check bot status
- `/setdm` - Set up role DM (legacy command)
- `/marketing` - Start marketing campaign
- `/add_get_now` - Add get now button

## 🎛️ Dashboard Features

### Role DM Management
- Set up automatic DMs for specific roles
- Custom message templates with variables
- Button customization (text, emoji, color)
- Claim role functionality
- Server logo integration

### Marketing Campaigns
- Target specific roles
- Schedule campaigns
- Track campaign performance
- Custom message templates

### Get Now Buttons
- Create interactive buttons
- Lead generation tracking
- Custom styling options

### Settings
- Server logo management
- Default template editing
- Test all bot functions
- Rate limit management

## 🔧 Configuration

### Environment Variables
- `BOT_TOKEN`: Your Discord bot token (set in bot.py)

### Database
- Uses SQLite for data storage
- Automatically creates necessary tables
- Data stored in `bot_data.db`

### File Structure
```
discord-affiliate-bot/
├── bot.py                 # Main bot code
├── templates/
│   └── dashboard.html     # Web dashboard
├── requirements.txt       # Python dependencies
├── start_dashboard.bat    # Windows startup script
├── data.json             # Role DM messages (auto-created)
├── bot_data.db           # Database (auto-created)
└── README.md             # This file
```

## 🛠️ Development

### Adding New Features
1. Modify `bot.py` for backend functionality
2. Update `templates/dashboard.html` for frontend
3. Add new API endpoints as needed
4. Test thoroughly before deployment

### API Endpoints
- `/api/status` - Bot status
- `/api/roles` - Get server roles
- `/api/channels` - Get server channels
- `/api/roledms` - Role DM management
- `/api/campaigns` - Marketing campaigns
- `/api/getnow` - Get now buttons
- `/api/leads` - Lead data
- `/api/emojis` - Server emojis
- `/api/server-logo` - Server logo management

## 🔒 Security

- **Never share your bot token**
- Keep your bot token secure
- Use environment variables for production
- Regularly update dependencies

## 📝 License

This project is for educational and personal use.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 🆘 Support

If you encounter any issues:
1. Check the console output for errors
2. Verify your bot token is correct
3. Ensure bot has proper permissions
4. Check Discord server settings

## 📊 Features Overview

| Feature | Status | Description |
|---------|--------|-------------|
| Role DMs | ✅ | Automatic DMs on role assignment |
| Marketing | ✅ | Targeted role campaigns |
| Get Now | ✅ | Interactive lead generation |
| Dashboard | ✅ | Web-based management interface |
| Templates | ✅ | Customizable message templates |
| Buttons | ✅ | Customizable button styling |
| Rate Limiting | ✅ | Spam protection |
| Auto-Refresh | ✅ | Automatic server data updates |

---

**Made with ❤️ for Discord communities**
