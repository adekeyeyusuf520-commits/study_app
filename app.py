from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["GET", "POST"])
def ask():
    answer = None
    if request.method == "POST":
        user_input = request.form["question"]
        try:
            model = genai.GenerativeModel("gemini-2.5-flash")
            response = model.generate_content(user_input)
            answer = response.text
        except Exception as e:
            answer = f"Error: {str(e)}"
    return render_template("ask.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
