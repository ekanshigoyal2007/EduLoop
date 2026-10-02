from fastapi import FastAPI
from pydantic import BaseModel
import os
from google import genai

app = FastAPI(title="EduLoop API")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    gemini_client = genai.Client(api_key=GEMINI_API_KEY)
else:
    gemini_client = None


class BookRequest(BaseModel):
    request: str


@app.get("/")
def home():
    return {
        "project": "EduLoop",
        "status": "online"
    }


@app.post("/find-book")
def find_book(data: BookRequest):

    if gemini_client is None:
        return {
            "success": False,
            "message": "Gemini API key is not configured."
        }

    try:
        response = gemini_client.models.generate_content(
            model="gemini-3.6-flash",
            contents=f"""
You are the EduLoop AI agent.

A student is looking for an academic book.

Student request:
{data.request}

Understand the request and provide a concise recommendation.
"""
        )

        return {
            "success": True,
            "agent": "EduLoop",
            "request": data.request,
            "recommendation": response.text
        }

    except Exception as e:
        return {
            "success": False,
            "message": str(e)
        }