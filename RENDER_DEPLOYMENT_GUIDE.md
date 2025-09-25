# Deploy Discord Affiliate Bot to Render

## 🚀 **Step-by-Step Render Deployment**

### **Prerequisites:**
- ✅ Your bot is working locally
- ✅ GitHub repository (or GitLab) with your code
- ✅ Render account (free tier available)

### **Step 1: Prepare Your Repository**

1. **Push your code to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial Discord Affiliate Bot setup"
   git branch -M main
   git remote add origin https://github.com/yourusername/discord-affiliate-bot.git
   git push -u origin main
   ```

### **Step 2: Deploy to Render**

#### **Option A: Using render.yaml (Recommended)**
1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click **"New +"** → **"Blueprint"**
3. Connect your GitHub repository
4. Render will automatically detect `render.yaml`
5. Click **"Apply"** to deploy

#### **Option B: Manual Setup**
1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click **"New +"** → **"Background Worker"**
3. Configure:
   - **Name**: `discord-affiliate-bot`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python bot.py`
   - **Plan**: `Free`

### **Step 3: Configure Environment Variables**

In your Render service settings, add these environment variables:

#### **Required Variables:**
```
DISCORD_BOT_TOKEN = YOUR_DISCORD_BOT_TOKEN_HERE
API_BASE_URL = https://base44.app/api/apps/68d1f85a602cecfca6c02c10/functions
BASE44_APP_ID = 68d1f85a602cecfca6c02c10
DISCORD_CLIENT_ID = 1420475643166068877
DISCORD_CLIENT_SECRET = YOUR_DISCORD_CLIENT_SECRET_HERE
```

#### **How to Add Variables:**
1. Go to your service in Render dashboard
2. Click **"Environment"** tab
3. Click **"Add Environment Variable"**
4. Add each variable above
5. Click **"Save Changes"**

### **Step 4: Deploy and Monitor**

1. **Deploy**: Click **"Deploy Latest Commit"**
2. **Monitor**: Watch the logs in real-time
3. **Verify**: Check that your bot connects to Discord

### **Expected Logs:**
```
✅ Starting Base44 Affiliate Bot...
✅ Base44 Platform: https://base44.app/api/apps/68d1f85a602cecfca6c02c10/functions
✅ Bot ID: 68d1f85a602cecfca6c02c10
✅ Logged in as Affiliate BOT base44#0116
✅ Bot is in 1 server(s)
✅ Connected to Base44 platform
✅ Bot started successfully
```

## 🔧 **Alternative Deployment Options**

### **Railway (Alternative to Render)**
1. Go to [Railway](https://railway.app)
2. Connect GitHub repository
3. Deploy with `Procfile` (already created)
4. Add environment variables

### **Heroku (Alternative)**
1. Go to [Heroku](https://heroku.com)
2. Create new app
3. Connect GitHub repository
4. Use `Procfile` for deployment
5. Add environment variables in Settings

### **DigitalOcean App Platform**
1. Go to [DigitalOcean](https://cloud.digitalocean.com)
2. Create new app
3. Connect repository
4. Configure as worker service
5. Add environment variables

## 📊 **Monitoring Your Deployed Bot**

### **Render Dashboard:**
- **Logs**: Real-time log monitoring
- **Metrics**: CPU and memory usage
- **Status**: Service health and uptime

### **Discord:**
- **Bot Status**: Online indicator
- **Server Count**: Number of connected servers
- **Activity**: Role assignments and DMs

### **Base44 Dashboard:**
- **Bot Status**: Health and performance
- **Campaigns**: Message templates and campaigns
- **Analytics**: User interactions and conversions

## 🛠️ **Troubleshooting Deployment**

### **Common Issues:**

#### **1. Bot Won't Start**
- Check environment variables are set correctly
- Verify Discord bot token is valid
- Check logs for specific error messages

#### **2. Bot Disconnects Frequently**
- Render free tier may have limitations
- Consider upgrading to paid plan
- Check bot token permissions

#### **3. Base44 API Errors**
- Normal for new deployments
- Bot handles errors gracefully
- Check Base44 dashboard for configuration

### **Debug Commands:**
```bash
# Check environment variables
echo $DISCORD_BOT_TOKEN

# Test bot connection
python -c "import discord; print('Discord.py version:', discord.__version__)"

# Verify imports
python -c "import bot; print('Bot module loaded successfully')"
```

## 🎉 **After Deployment**

### **Your Bot Will:**
- ✅ Run 24/7 on Render
- ✅ Automatically restart if it crashes
- ✅ Connect to Discord and Base44
- ✅ Process role assignments and campaigns
- ✅ Log all activities for monitoring

### **Next Steps:**
1. **Test the deployed bot** in your Discord server
2. **Configure campaigns** via Base44 dashboard
3. **Monitor performance** through Render logs
4. **Set up alerts** for bot downtime

## 💰 **Cost Considerations**

### **Render Free Tier:**
- ✅ Free for small bots
- ✅ 750 hours/month
- ⚠️ May sleep after inactivity
- ⚠️ Slower cold starts

### **Render Paid Plans:**
- ✅ Always-on service
- ✅ Faster performance
- ✅ Better monitoring
- 💰 Starting at $7/month

Your Discord Affiliate Bot is ready for professional deployment! 🚀
