
# 🩺 AI Health Assistant

A secure, AI-powered health chatbot that uses Retrieval-Augmented Generation (RAG) to deliver intelligent, real-time responses grounded in internal clinical documentation. This project showcases applied Gen AI engineering, including vector search, document embedding, and integration with Gemini 1.5 via Google’s Generative AI SDK.

---

## 🚀 Live Demo  
**Hosted Frontend:** [AI Health Assistant](https://mellow-bunny-240a24.netlify.app/)

---

## 💡 Project Purpose  

This project was built to demonstrate practical experience in:  
- End-to-end RAG architecture  
- Embedding-based search using FAISS  
- Real-time LLM integration with Google's Gemini 1.5  
- Secure, compliant chatbot design in a healthcare context  

It simulates how modern AI assistants can support clinicians and patients with internal knowledge without exposing or storing user data.

---

## ⚙️ Core Features

- **LLM-Backed Natural Language Understanding**: User queries processed via Gemini 1.5 Flash.
- **Retrieval-Augmented Generation (RAG)**: Combines vector similarity search with prompt augmentation to ground responses.
- **Custom Document Ingestion Pipeline**: Markdown-based internal clinical resources parsed, embedded, and indexed.
- **FAISS Vector Search**: Enables fast retrieval over dense sentence-transformer embeddings.
- **Frontend Chat Interface**: Lightweight, responsive UI for real-time interactions.
- **Stateless & Secure**: No user data stored. Designed with HIPAA/GDPR in mind.

---

## 🧱 Tech Stack

| Layer | Technology |
|-------|------------|
| LLM | Gemini 1.5 (via `google.generativeai`) |
| Embeddings | `sentence-transformers` (`all-MiniLM-L6-v2`) |
| Vector Store | FAISS |
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript |

---

## 🗂️ Project Structure

```
AI_Health_Assistant/
├── backend/
│   ├── app/
│   │   ├── main.py           # Chat API endpoint
│   │   ├── ingest_docs.py    # Document parsing & vector storage
│   │   ├── vector_store/     # FAISS index + metadata
│   │   └── docs/             # Knowledge base (.md files)
│   ├── requirements.txt
│   └── Procfile
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
└── README.md
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/daniel-agblevor/AI_Health_Assistant.git
cd AI_Health_Assistant
```

### 2. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
```

### 3. Configure Environment
Create an `.env` file in the `app/` directory with:
```env
GOOGLE_API_KEY=your_gemini_api_key
```

### 4. Ingest Internal Documents
Add your `.md` files to `app/docs/`, then:
```bash
python app/ingest_docs.py
```

### 5. Start the Backend Server
```bash
python app/main.py
```

### 6. Frontend
Open `frontend/index.html` in a browser to access the UI.

---

## ✅ Key Engineering Highlights

- **RAG Pipeline**: Built from scratch with Flask, using FAISS for top-K document retrieval, then injecting relevant context into Gemini prompts.
- **Custom Embedding Workflow**: Efficiently processes unstructured clinical markdown using sentence-transformers.
- **LLM Integration**: Programmatic use of Gemini 1.5 Flash with streamed response parsing.
- **Secure, Stateless Architecture**: No PII stored or logged. Fully GDPR/HIPAA aligned.

---

## 🧠 What I Gained from Building This

- ✅ **Hands-on RAG Architecture**: Implemented retrieval-augmented generation from scratch, integrating dense embeddings, vector similarity search, and prompt engineering.
- ✅ **LLM API Mastery**: Integrated Gemini 1.5 Flash with secure key management and response handling using Google's `generativeai` SDK.
- ✅ **Efficient Document Embedding Pipelines**: Built a scalable ingestion system for Markdown files using `sentence-transformers` and FAISS.
- ✅ **Frontend-Backend Integration**: Delivered a seamless chat experience by connecting a custom frontend to a Flask backend with real-time response rendering.
- ✅ **Security-Conscious Development**: Ensured GDPR and HIPAA alignment by keeping the architecture stateless and avoiding data persistence or logging.
- ✅ **Deployment-Ready Workflow**: Structured for deployment with clearly separated concerns, Procfile support, and environment-based config.

---

## 🔐 Notes on Safety & Limitations

- This is an AI assistant prototype for demonstration only.
- It does **not provide medical advice or diagnosis**.
- Responses are generated from internal documentation only—no external API lookups or data persistence.

---

## 📜 License
MIT License. See `LICENSE` file.

---

## 🤝 Contributions
Pull requests are welcome. For issues or enhancements, please open a ticket.