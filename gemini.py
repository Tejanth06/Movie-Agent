import requests
from config import GEMINI_API_KEY


def ask_gemini(prompt):

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key={GEMINI_API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    response = requests.post(
        url,
        headers=headers,
        json=data
    )

    if response.status_code != 200:
        return f"❌ Gemini Error:\n{response.text}"

    result = response.json()

    return result["candidates"][0]["content"]["parts"][0]["text"]