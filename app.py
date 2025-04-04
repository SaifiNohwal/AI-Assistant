from flask import Flask, render_template, request
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

app = Flask(__name__)

def get_gemini_response(prompt):
    """Generates a response using Google Gemini API."""
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        function_type = request.form["function_type"]
        user_input = request.form["user_input"]

        # Function-specific prompts
        prompts = {
            "question": f"Answer this question concisely: {user_input}",
            "summarize": f"Summarize the following text:\n{user_input}",
            "creative": f"Write something creative about: {user_input}",
            "advice": f"Give me advice on: {user_input}",
        }

        prompt = prompts.get(function_type, "Please enter a valid query.")
        response = get_gemini_response(prompt)

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
