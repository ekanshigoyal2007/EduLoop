import os
from google import genai

api_key = os.getenv("GEMINI_API_KEY")

print("API key found:", bool(api_key))

if not api_key:
    exit()

client = genai.Client(api_key=api_key)

try:
    chat = client.chats.create(
        model="gemini-3.6-flash"
    )

    response = chat.send_message(
        message="Reply with exactly: EDULOOP AI WORKS"
    )

    print("RESULT:")
    print(response.text)

except Exception as e:
    print("ERROR:")
    print(type(e).__name__)
    print(e)
