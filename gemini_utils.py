import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def reconstruct_text(fragment):
    prompt = f"""
    You are an AI historian reconstructing old internet messages.
    Fill in the missing words and provide a natural, contextually accurate version.
    Fragment: "{fragment}"
    Respond only with the reconstructed text.
    """
    model = genai.GenerativeModel("models/gemini-2.5-flash-preview-09-2025")
    response = model.generate_content(prompt)
    return response.text.strip()
