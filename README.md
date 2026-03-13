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
