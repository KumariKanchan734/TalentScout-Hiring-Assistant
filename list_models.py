import os
import json
import urllib.request
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

try:
    if not api_key:
        raise ValueError("GROQ_API_KEY is not set in the environment.")
    
    url = "https://api.groq.com/openai/v1/models"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {api_key}"})
    
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
    
    print("Available Groq Models:")
    for m in data.get("data", []):
        print(f"- {m.get('id')}")
except Exception as e:
    print("Error listing models:", str(e))
