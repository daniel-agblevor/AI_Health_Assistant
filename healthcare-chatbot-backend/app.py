from flask import Flask, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv
from flask_cors import CORS
import textwrap


# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

# Define a route for the chatbot
@app.route('/chat', methods=['POST'])
def ask():
    word_limit = 300
    instruction = f'''
You are a healthcare chatbot. You will be given a prompt and you will respond to it in a precise and concise manner.
Be brief and precise, respond with no more than {word_limit} words. List the key points in bullet points.
'''
    data = request.get_json()
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400
    # Generate a response using the Generative AI model
    response = model.generate_content(instruction + prompt)
    return jsonify({'reply': response.text}), 200


# Define a route for the home page
@app.route('/', methods=['GET'])
def home():
    return "Healthcare Chatbot API is running!"


if __name__ == '__main__':
    app.run(debug=True)