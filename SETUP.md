# Quick Setup Guide

## ⚡ 1-Minute Setup

### Step 1: Clone & Install
```bash
git clone https://github.com/YOUR_USERNAME/talentscout-bot.git
cd talentscout-bot
python -m venv .venv
.venv\Scripts\activate  # Windows
# OR
source .venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

### Step 2: Configure API Key
```bash
copy .env.example .env  # Windows
# OR
cp .env.example .env  # macOS/Linux
```

Edit `.env`:
```
GROQ_API_KEY=gsk_your_actual_api_key_here
```

Get your free Groq API key: https://console.groq.com

### Step 3: Run
```bash
npm start
```

Or directly:
```bash
streamlit run app.py
```

**Open:** http://localhost:8501

---

## ✅ Verification Checklist

After setup, verify:

- [ ] App loads at http://localhost:8501
- [ ] Can start a new interview
- [ ] Bot greets you with "Welcome to TalentScout"
- [ ] Can input responses in chat
- [ ] No error messages in terminal

---

## 🆘 Quick Troubleshooting

| Issue | Solution |
|-------|----------|
| "LLM not initialised" | Check `.env` file has valid `GROQ_API_KEY` |
| "site cannot be reached" | Wait 10s, check terminal shows "Local URL: 8501" |
| "ModuleNotFoundError" | Run `pip install -r requirements.txt` |
| "Port 8501 in use" | Kill process or use `streamlit run app.py --server.port 8502` |

---

## 📚 Full Documentation

- **Setup Issues?** → See README.md
- **Deployment?** → See DEPLOYMENT.md
- **Contributing?** → See CONTRIBUTING.md (if available)

---

**Done! 🚀 You're ready to go.**
