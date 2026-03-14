# GitHub Setup & Deployment Guide

## 📋 Pre-Push Checklist

Before pushing to GitHub, ensure:

- ✅ `.env` file is NOT committed (should be in `.gitignore`)
- ✅ `__pycache__/` is NOT committed
- ✅ `.venv/` is NOT committed
- ✅ `candidates_data.json` is NOT committed (local test data)
- ✅ All source files are committed
- ✅ `.env.example` is committed (without actual keys)
- ✅ `requirements.txt` is updated with versions
- ✅ `README.md` is comprehensive
- ✅ `.gitignore` is properly configured

---

## 🚀 GitHub Push Steps

### Step 1: Initialize Git (if not already done)
```bash
cd talentscout_bot
git init
git config user.email "your-email@example.com"
git config user.name "Your Name"
```

### Step 2: Add All Files
```bash
git add .
```

### Step 3: Verify What Will Be Committed
```bash
git status
```

**Important:** Make sure `.env` is NOT listed. If it is:
```bash
git rm --cached .env
git commit -m "Remove .env from tracking"
```

### Step 4: Commit
```bash
git commit -m "Initial commit: TalentScout Hiring Assistant Bot

- AI-powered candidate screening chatbot
- Streamlit frontend with LangChain + Groq LLM
- Automated candidate data storage
- Ready for deployment"
```

### Step 5: Create GitHub Repository
1. Go to [GitHub](https://github.com/new)
2. Create new repository: `talentscout-bot`
3. **DO NOT** add README, .gitignore, or license (you already have these)

### Step 6: Add Remote & Push
```bash
git remote add origin https://github.com/YOUR_USERNAME/talentscout-bot.git
git branch -M main
git push -u origin main
```

---

## 🌐 Deployment

### Option 1: Heroku Deploy
```bash
# Install Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# Login
heroku login

# Create app
heroku create your-app-name

# Set environment variables
heroku config:set GROQ_API_KEY=your_groq_key_here -a your-app-name

# Deploy
git push heroku main

# View logs
heroku logs --tail -a your-app-name
```

### Option 2: Railway Deploy
1. Go to [Railway.app](https://railway.app)
2. Login with GitHub
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose your repository
6. Add environment variable: `GROQ_API_KEY`
7. Deploy!

### Option 3: Docker Deployment
```bash
# Build image
docker build -t talentscout-bot .

# Run container
docker run -e GROQ_API_KEY=your_key -p 8501:8501 talentscout-bot

# Or use docker-compose
docker-compose up --build
```

---

## 📦 Files to Include in Repository

```
✅ app.py
✅ bot_logic.py
✅ database.py
✅ prompts.py
✅ list_models.py
✅ requirements.txt
✅ package.json
✅ .env.example
✅ .gitignore
✅ README.md
✅ Procfile
✅ Dockerfile
✅ docker-compose.yml
✅ .streamlit/config.toml

❌ .env (NEVER commit!)
❌ __pycache__/
❌ .venv/
❌ candidates_data.json (if containing test data)
```

---

## 🔐 Security Best Practices

1. **Never commit `.env` file**
   - It contains sensitive API keys
   - Use `.env.example` instead

2. **For Deployment:**
   - Use platform-specific secret management
   - Set `GROQ_API_KEY` as environment variable
   - Never hardcode credentials

3. **Repository Settings:**
   - Enable branch protection
   - Require PR reviews
   - Enable automated security scanning

---

## 📝 Useful Git Commands Reference

```bash
# Check status
git status

# Add specific file
git add filename.py

# Add all files
git add .

# Commit
git commit -m "Your message"

# Push to main
git push origin main

# Pull latest changes
git pull origin main

# Create new branch
git checkout -b feature/new-feature

# Switch branch
git checkout main

# Delete local branch
git branch -d feature/old-feature

# View commit history
git log --oneline

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1
```

---

## ✨ Post-Deployment Verification

After deploying:

1. ✅ Visit the deployed URL
2. ✅ Start a test interview
3. ✅ Verify LLM is responding
4. ✅ Check that data is being saved
5. ✅ Test on mobile browser

---

## 🆘 Deployment Troubleshooting

### "Cannot find module" error
```bash
# Make sure requirements.txt is in root
# Reinstall dependencies
pip install -r requirements.txt
```

### "Port already in use"
```bash
# Find process using port 8501
netstat -ano | findstr :8501

# Kill process (replace PID)
taskkill /PID <PID> /F
```

### "GROQ_API_KEY not found"
```bash
# Verify environment variable is set
echo $GROQ_API_KEY

# For Heroku
heroku config -a your-app-name
```

---

## 📊 Repository Structure Preview

After pushing to GitHub, your repo should look like:

```
talentscout-bot/
├── .github/
│   └── workflows/          # (Optional) CI/CD pipelines
├── .streamlit/
│   └── config.toml
├── .gitignore
├── .env.example
├── Dockerfile
├── Procfile
├── README.md
├── DEPLOYMENT.md           # This file
├── app.py
├── bot_logic.py
├── database.py
├── list_models.py
├── prompts.py
├── package.json
├── requirements.txt
└── docker-compose.yml
```

---

**Happy Deploying! 🎉**
