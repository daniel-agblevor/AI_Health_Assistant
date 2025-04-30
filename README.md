# 🩺 AI Healthcare Chatbot

A secure, modern AI-powered chatbot for healthcare providers. This assistant delivers real-time, natural language responses to health-related questions grounded in your institution’s internal documentation.

---

## 📌 Features

- Natural language query handling
- Retrieval-augmented generation (RAG)
- Gemini 1.5 Flash for fast and smart responses
- Session-based chat history with reset and loading states
- Clear disclaimers and privacy policy display

---

## 🧱 Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Embeddings**: `sentence-transformers` (`all-MiniLM-L6-v2`)
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
│   └── docs/                 # Internal .md documents
├── frontend/
│   ├── index.html            # Chat interface
│   ├── style.css             # UI styling
│   └── app.js                # Frontend logic
├── .env.example              # Environment variable template
└── README.md
```

---

## 🚀 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/daniel-agblevor/AI_Health_Assistant.git
cd healthcare-chatbot
```

### 2. Install Backend Dependencies

```bash
cd app
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file inside the `app/` directory:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

### 4. Ingest Internal Documents

Place your internal `.md` files into `app/docs/`, then run:

```bash
python ingest_docs.py
```

This will embed the documents into the vector database for use during chat.

### 5. Run the Backend Server

```bash
python main.py
```

---

## 💬 Using the Chatbot

### Frontend Access

Open the file `frontend/index.html` in your browser to use the chatbot.

### Functionalities

- Enter a question into the text box
- Click "Send" to receive a response
- Use "Reset" to clear the chat history
- Wait for the loading spinner while responses are generated

---

## 🔐 Compliance & Safety

- ⚠️ No medical advice — only helpful suggestions and document references
- ❌ No user data is stored or logged
- 🔍 No diagnoses or treatment suggestions are provided
- 🔐 No personal information is collected

---

## ✅ Goals

- Answers at least 90% of document-based questions accurately
- Response time under 5 seconds
- Fully responsive UI (mobile + desktop)

---

## 📖 License

MIT License

---

## 🤝 Contributions

Pull requests are welcome. For bugs or feature requests, please open an issue.