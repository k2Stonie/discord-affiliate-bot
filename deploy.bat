@echo off
echo 🚀 Preparing Discord Affiliate Bot for Deployment
echo ==================================================

REM Check if git is initialized
if not exist ".git" (
    echo 📁 Initializing Git repository...
    git init
    git branch -M main
)

REM Add all files
echo 📦 Adding files to Git...
git add .

REM Commit changes
echo 💾 Committing changes...
git commit -m "Deploy Discord Affiliate Bot to cloud platform

- Added Render deployment configuration
- Added runtime.txt for Python version
- Added comprehensive deployment guides
- Bot ready for 24/7 cloud hosting"

echo.
echo ✅ Files committed to Git!
echo.
echo Next steps:
echo 1. Create a GitHub repository
echo 2. Add remote origin: git remote add origin https://github.com/yourusername/discord-affiliate-bot.git
echo 3. Push to GitHub: git push -u origin main
echo 4. Deploy to Render using the deployment guide
echo.
echo 📖 See RENDER_DEPLOYMENT_GUIDE.md for detailed instructions
pause
