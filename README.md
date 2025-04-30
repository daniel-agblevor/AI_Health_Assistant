# 🩺 AI Healthcare Assistant Chatbot

This is a secure, AI-powered chatbot that provides real-time responses to health-related inquiries based on internal healthcare documents. It uses **Google Gemini**, **Retrieval-Augmented Generation (RAG)**, and a custom frontend.

---

## 🚀 Features

- ✅ Accepts natural language health-related questions
- ✅ Provides answers from internal healthcare documents (SOPs, policies, guidelines)
- ✅ Uses Gemini AI for natural language generation
- ✅ Responsive and user-friendly frontend
- ✅ Secure, disclaimer-compliant, no PII logging

---

## 🧱 Project Structure

```bash
project-root/
│
├── healthcare-chatbot-backend/
│   ├── app.py                   # Flask backend
│   ├── ingest_docs.py           # Ingest and embed documents
│   ├── utils/
│   │   ├── file_loader.py       # File parsing utilities
│   │   └── rag.py               # RAG logic (retrieval + generation)
│   ├── docs/                    # Internal healthcare documents
│   ├── requirements.txt         # Python dependencies
│   ├── .env.example             # Environment config sample
│   └── Procfile                 # For deployment (Heroku)
│
├── healthcare-chatbot-frontend/
│   ├── index.html               # Web UI
│   ├── style.css                # Styles
│   └── app.js                   # Frontend logic
│
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-healthcare-chatbot.git
cd ai-healthcare-chatbot
```

### 2. Set Up Backend

```bash
cd healthcare-chatbot-backend
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
cp .env.example .env
# Fill in your actual API keys and secrets in .env
```

### 4. Prepare Internal Documents

Place your `.pdf`, `.docx`, `.txt`, or `.csv` documents in the `docs/` folder, then run:

```bash
python ingest_docs.py
```

This will parse, embed, and index the documents using FAISS.

### 5. Run the Backend

```bash
python app.py
# The API will be available at http://127.0.0.1:5000
```

### 6. Run the Frontend

Open `healthcare-chatbot-frontend/index.html` in a browser. It will call the backend at `/chat`.

---

## 📬 API Endpoint

### `POST /chat`

**Request Body:**

```json
{
  "prompt": "What should I do if a patient shows signs of severe allergic reaction?"
}
```

**Response:**

```json
{
  "reply": "• Monitor airway, breathing, circulation\n• Administer epinephrine immediately..."
}
```

---

## 📦 Deployment

- Docker or cloud platforms like Render, Heroku, or EC2
- Ensure your `.env` file is set up
- Use HTTPS and proper CORS settings

---

## 📌 Disclaimers

- This chatbot does **not provide medical advice**
- No data is stored or logged
- It should be used for **educational and internal support only**

---

## 🤝 Contributions

Pull requests are welcome! Please fork the repo and open an issue or PR for discussion.

---

## 📄 License

MIT License

```