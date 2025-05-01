from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv
from core.rag import retrieve_relevant_chunks


load_dotenv() # Load environment variables from .env file

os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")
genai.configure()

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

@app.route("/chat", methods=["POST"])
def chat():
    user_query = request.json.get("prompt")
    print(f"Received user query: {user_query}") # Add this print statement
    context = retrieve_relevant_chunks(user_query)
    print(f"Retrieved context:\n{context}") # Add this print statement
    full_prompt = f"""
You are a healthcare assistant, Ella, at DanielAGB Medical Centre that offers basic health services. Keep your replies short — no more than 200 words.
with this:
context: {context}
question: {user_query}
Your job is to:
Use the context to answer the question as helpfully and clearly as possible.
If the context has some related info, use what you can to give a useful answer.
If the context has no helpful info, say so politely and give a helpful suggestion based on your general healthcare knowledge.
Important: Do not mention the words "context", "document", or "provided text" in your reply. Just speak naturally, like a helpful human assistant.
"""

    try:
        response = model.generate_content(full_prompt)
        return jsonify({"response": response.text})
    except Exception as e:
        print(f"Error during Gemini response: {e}")
        return jsonify({"response": "Sorry, something went wrong."}), 500

@app.route("/", methods=["GET"])
def health_check():
    return "OK", 200

if __name__ == '__main__':
    app.run(debug=True) # enabling debug mode for more verbose output