# 🩺 AI Healthcare Chatbot

A secure, modern AI-powered chatbot for healthcare providers. This web-based assistant delivers real-time, natural language responses to health-related questions grounded in your institution’s internal documentation.

---

## 📌 Features

- Natural language health-related query handling
- Retrieval-augmented generation (RAG) using internal documents
- Gemini 1.5 Flash integration for response generation
- Session-based chat history with reset and loading states
- Clear disclaimers and privacy policy

---

## 🧱 Tech Stack

- **Frontend**: HTML, CSS, Vanilla JS
- **Backend**: Python (Flask)
- **Embedding**: `sentence-transformers` (`all-MiniLM-L6-v2`)
- **Vector DB**: FAISS or ChromaDB
- **LLM**: Gemini 1.5 via `google.generativeai`

---

## 📂 Project Structure

```
healthcare-chatbot/
├── app/
│   ├── main.py               # Flask backend
│   ├── ingest_docs.py        # Document parser & embedding
│   ├── utils.py              # Helper functions
│   └── docs/                 # Your internal .md documents
├── frontend/
│   ├── index.html            # Chat interface
│   ├── style.css             # UI styling
│   └── app.js                # Frontend logic
├── .env.example              # Environment variables template
└── README.md
```

---

## 🚀 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/daniel-agblevor/AI_Health_Assistant.git
cd healthcare-chatbot
```

### 2. Install Dependencies (Backend)

```bash
cd app
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Configure `.env`

Create a `.env` file in the `app/` directory based on `.env.example` and add your Gemini API key.

```env
GOOGLE_API_KEY=your_gemini_api_key
```

### 4. Ingest Internal Docs

Place your `.md`, `.pdf`, `.txt`, `.csv`, or `.docx` files into the `app/docs/` folder, then run:

```bash
python ingest_docs.py
```

This will parse and embed your documents into FAISS or ChromaDB.

### 5. Run Backend API

```bash
python main.py
```

### 6. Open Frontend

Navigate to `frontend/index.html` in your browser or deploy with a static hosting service (e.g. Vercel, Netlify).

---

## 🧪 Testing the App

- Use the chat box to enter questions.
- Watch for live responses, formatted replies, and disclaimers.
- Use the "Reset" button to start a new session.

---

## 📦 Deployment

You can use Docker or your preferred cloud service.

### Docker

```bash
docker-compose up --build
```

Make sure your `.env` file is mounted properly in the backend container.

---

## 🔐 Compliance & Safety

- ⚠️ No medical advice — responses include disclaimers.
- ❌ No user data is stored or logged.
- 🧾 No diagnoses or treatment suggestions are made.
- 🔐 PII handling is strictly avoided.

---

## ✅ Acceptance Criteria

- 📄 Answers 90%+ of document-based queries accurately
- ⚡ Responds in under 5 seconds
- 📱 Works on all screen sizes
- 🔐 Secure deployment
- 🔧 Admin panel works for uploading and managing docs

---

## 📖 License

MIT License

---

## 🤝 Contributions

PRs welcome. For feature requests or bugs, open an issue.