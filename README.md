# TalentScout Hiring Assistant 🤖

An **AI-powered hiring assistant chatbot** built using **Streamlit, LangChain, and Groq's LLaMA model**.

The chatbot conducts an **initial candidate screening interview**, collects important candidate details, asks technical questions based on the candidate's tech stack, and stores the responses in a structured JSON database.

This project demonstrates how **Large Language Models (LLMs)** can be used to automate **candidate screening in recruitment workflows**.

---

# Features

### Conversational Candidate Screening

The bot collects candidate information through a natural conversation:

* Full Name
* Email Address
* Phone Number
* Years of Experience
* Current Location
* Desired Position
* Tech Stack

The chatbot asks **one or two questions at a time** to maintain a smooth interview experience.

---

### Technical Skill Evaluation

After collecting the candidate's **tech stack**, the assistant generates **technical questions** related to those technologies.

---

### Intelligent Conversation Flow

The chatbot:

* Maintains conversation context
* Handles off-topic responses
* Guides the candidate back to the interview flow
* Completes the interview gracefully

---

### Automatic Candidate Data Storage

Once the interview is completed:

* The chatbot generates structured **JSON data**
* The system extracts the data
* Candidate information is saved in:

```
candidates_data.json
```

---

# Tech Stack

| Layer                 | Technology              |
| --------------------- | ----------------------- |
| Frontend              | Streamlit               |
| LLM Framework         | LangChain               |
| LLM Provider          | Groq                    |
| Model                 | LLaMA 3.3 70B Versatile |
| Data Storage          | Local JSON database     |
| Environment Variables | python-dotenv           |

---

# Project Structure

```
talentscout_bot/
│
├── app.py                   # Streamlit application interface
├── bot_logic.py             # Core chatbot logic and LLM interaction
├── database.py              # Handles saving candidate data
├── prompts.py               # System prompt and interview instructions
├── list_models.py           # Utility to list available Groq models
├── candidates_data.json     # Stored candidate records
├── requirements.txt         # Project dependencies
├── .env                     # API key configuration
└── .env.example             # Environment variable template
```

---

# Module Responsibilities

| File                   | Purpose                                          |
| ---------------------- | ------------------------------------------------ |
| `app.py`               | Streamlit interface and chat UI                  |
| `bot_logic.py`         | Builds Groq LLM and manages conversation logic   |
| `prompts.py`           | Contains the system prompt guiding the interview |
| `database.py`          | Stores candidate data in JSON format             |
| `list_models.py`       | Lists available Groq models                      |
| `candidates_data.json` | Local storage for candidate information          |

---

# Quick Start

## Prerequisites
- Python 3.8+
- Node.js 14+ (optional, for npm scripts)
- Groq API Key from [console.groq.com](https://console.groq.com)

## Installation Steps

### 1. Clone & Setup
```bash
git clone <your-repo-url>
cd talentscout_bot
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API Key
Create `.env` file from template:
```bash
# Windows
copy .env.example .env

# macOS/Linux
cp .env.example .env
```

Edit `.env` and add your Groq API key:
```
GROQ_API_KEY=gsk_your_actual_key_here
```

### 4. Run Application

**Option A: Using npm (recommended)**
```bash
npm start
```

**Option B: Using Streamlit directly**
```bash
streamlit run app.py
```

Visit: **http://localhost:8501**

---

# Deployment Guide

## ✅ Troubleshooting Common Errors

### Error: "LLM not initialised. Please ensure GROQ_API_KEY is correctly configured."

**Causes & Solutions:**

1. ✋ **Missing `.env` file**
   - Create `.env` from `.env.example`
   - Ensure `.env` is in the project root directory
   - Check it's not in `.gitignore` (it should be!)

2. 🔑 **Invalid or Empty API Key**
   - Verify your Groq API key is correct
   - Check it doesn't have extra spaces
   - Get a new key from [console.groq.com](https://console.groq.com)

3. 📦 **Missing Dependencies**
   ```bash
   pip install python-dotenv langchain langchain-groq
   ```

4. 🔄 **Restart the Application**
   - Stop: `Ctrl+C`
   - Run: `npm start`

### Error: "site cannot be reached" on localhost

**Solutions:**
- ✅ Is the app running? Check terminal output
- ⏳ Wait 5-10 seconds for Streamlit to fully initialize
- 🔌 Check if port 8501 is in use: `netstat -ano | findstr 8501`
- 🛡️ Check firewall/antivirus isn't blocking port 8501
- 🌐 Try `http://127.0.0.1:8501` instead of `localhost:8501`

### Error: "ModuleNotFoundError: No module named..."

**Solution:**
```bash
# Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

---

## 🚀 Deployment Options

### Option 1: Local Machine
Already covered above!

### Option 2: Heroku
```bash
# Create Procfile
echo "web: streamlit run --server.port \$PORT --server.headless true app.py" > Procfile

# Deploy
heroku create your-app-name
heroku config:set GROQ_API_KEY=your_key_here
git push heroku main
```

### Option 3: Railway/Render
1. Push to GitHub (see below)
2. Connect repo to Railway/Render
3. Set environment variables:
   - `GROQ_API_KEY=your_key_here`
4. Deploy!

### Option 4: Docker
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "app.py", "--server.port", "8501"]
```

### Option 5: AWS/Google Cloud
1. Push to GitHub
2. Use Cloud Run or App Engine
3. Set `GROQ_API_KEY` environment variable
4. Deploy!

---

## 📝 Environment Variables Setup for Deployment

**IMPORTANT:** Never commit `.env` file to Git!

For each platform:

**Heroku:**
```bash
heroku config:set GROQ_API_KEY=your_key
```

**Railway/Render:** Use dashboard UI

**Docker Compose:**
```yaml
environment:
  - GROQ_API_KEY=your_key
```

**AWS/GCP:** Use Secrets Manager or equivalent

---

## ✨ Key Files Checklist

Before pushing to GitHub:

- ✅ `.env` is in `.gitignore` (sensitive data)
- ✅ `.env.example` has placeholder values (for reference)
- ✅ `requirements.txt` has all dependencies
- ✅ `README.md` has setup instructions
- ✅ `package.json` has npm start script
- ✅ Virtual environment `.venv` is in `.gitignore`

---

---

# Prerequisites

Before running the project, ensure you have:

* **Python 3.10 or higher**
* A **Groq API Key**

Get a Groq API key from:

```
https://console.groq.com
```

---

# Installation & Setup

## 1 Clone the repository

```
git clone <your-repository-url>
cd talentscout_bot
```

---

## 2 Create a virtual environment

```
python -m venv venv
```

Activate the environment:

Windows

```
venv\Scripts\activate
```

Linux / macOS

```
source venv/bin/activate
```

---

## 3 Install dependencies

```
pip install -r requirements.txt
```

---

## 4 Configure environment variables

Create a `.env` file and add your Groq API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

## 5 Run the application

Start the Streamlit server:

```
streamlit run app.py
```

The application will open at:

```
http://localhost:8501
```

---

# How It Works

1. The user opens the Streamlit application.
2. The chatbot greets the candidate.
3. The bot collects personal and professional information.
4. Based on the candidate's **tech stack**, technical questions are generated.
5. The candidate answers the questions through chat.
6. At the end of the interview:

   * Structured candidate data is generated.
   * Data is extracted and stored in `candidates_data.json`.

---

# Example Candidate Record

```
{
    "full_name": "John Doe",
    "email": "john@example.com",
    "phone": "+91-9876543210",
    "years_of_experience": "3",
    "desired_position": "Backend Developer",
    "current_location": "Delhi, India",
    "tech_stack": ["Python", "Django", "PostgreSQL"],
    "timestamp": "2026-03-13T19:25:00"
}
```

---

# Future Improvements

Possible enhancements:

* Resume upload and parsing
* Candidate ranking system
* Recruiter dashboard
* Integration with real ATS systems
* Database integration (MongoDB / PostgreSQL)
* Email notifications for recruiters

---

# License

This project is intended for **educational and demonstration purposes**.
