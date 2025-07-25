import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set")

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

headers = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": api_key,
}

def get_gemini_response(prompt: str) -> str:
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        try:
            result = response.json()
            return result["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            return f"Error: {e}"
    else:
        return f"Error: {response.status_code} - {response.text}"

#test
if __name__ == "__main__":
    
    user_input = input("Enter a prompt: ") 
    response = get_gemini_response(user_input)

    print(f"Gemini yaniti: {response}")