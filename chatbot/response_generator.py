# import google.generativeai as genai
# import os

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# model = genai.GenerativeModel("gemini-pro")

# def generate_response(context: str, question: str) -> str:
#     prompt = f"""
# You are a financial data assistant.
# Answer ONLY using the context below.
# If answer is missing say exactly:
# "Sorry can not find the answer"

# Context:
# {context}

# Question:
# {question}
# """
#     response = model.generate_content(prompt)
#     return response.text.strip()



# import os
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# model = genai.GenerativeModel("models/gemini-flash-latest")

# def generate_response(context, question):
#     prompt = f"""
# You are a financial assistant.
# Answer ONLY using the context below.
# If the answer is missing say exactly:
# "Sorry can not find the answer"

# Context:
# {context}

# Question:
# {question}
# """
#     return model.generate_content(prompt).text.strip()



import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini only if key exists
if API_KEY:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("models/gemini-flash-latest")
else:
    model = None


def generate_response(context: str, question: str) -> str:
    """
    Uses Gemini ONLY to rephrase verified context.
    If Gemini is unavailable or fails, returns context directly.
    """

    # If model is not available, skip LLM entirely
    if model is None:
        return context

    try:
        prompt = f"""
You are a financial assistant.
Answer ONLY using the context below.
If the answer is missing say exactly:
"Sorry can not find the answer"

Context:
{context}

Question:
{question}
"""
        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        # Absolute safety net
        print("Gemini failed, returning raw context.")
        print("Reason:", str(e))
        return context
