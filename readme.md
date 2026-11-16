# NITAverse 🎓🤖

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/Orchestration-LangChain-1C3C3C.svg)](https://www.langchain.com/)
[![Gemini](https://img.shields.io/badge/LLM-Google%20Gemini%202.0%20Flash-4285F4.svg)](https://ai.google.dev/)
[![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-FC521F.svg)](https://www.trychroma.com/)

**NITAverse** is an intelligent, domain-specific Retrieval-Augmented Generation (RAG) virtual assistant designed for the students, faculty, and aspirants of the **National Institute of Technology, Agartala (NITA)**.

Instead of navigating through hundreds of scattered circulars, unstructured PDFs, and static web pages, **NITAverse** allows users to ask natural language questions and receive accurate, grounded answers backed by official institute notices.

---

## 🌟 Key Features

- **Automated Campus Web Crawler**: Discovers, scrapes, and parses official university URLs, faculty profiles, and departmental information.
- **Notice & PDF Ingestion Pipeline**: Scrapes circulars, admission notices, fee structures, and examination rules, parsing both digital text and tabular data.
- **Clean Vector Embeddings**: Uses high-performance local embeddings (`sentence-transformers/all-MiniLM-L6-v2`) and persistent vector storage with **ChromaDB**.
- **Context-Grounded LLM Responses**: Employs **Google Gemini 2.0 Flash** via LangChain LCEL with strict grounding to eliminate hallucinations.
- **REST API Backend**: Scalable **FastAPI** service serving `/chat` query endpoints with validation.
- **Interactive UI**: Clean, responsive **Streamlit** chat interface styled with NIT Agartala's official institutional branding.

---

## 🏗️ System Architecture

```text
  [ NIT Agartala Portal (nita.ac.in) ]
                   │
                   ▼
  ┌─────────────────────────────────┐
  │  1. Data Ingestion & Crawling    │  ──> PDF Downloader & Link Correcter
  └─────────────────────────────────┘
                   │
                   ▼
  ┌─────────────────────────────────┐
  │  2. Text Extraction & Cleaning   │  ──> pdfplumber, regex cleaning, JSON schema
  └─────────────────────────────────┘
                   │
                   ▼
  ┌─────────────────────────────────┐
  │  3. Chunking & Vector Storage    │  ──> RecursiveCharacterTextSplitter
  │     (ChromaDB / all-MiniLM-L6)  │
  └─────────────────────────────────┘
                   │
       ┌───────────┴───────────┐
       ▼                       ▼
┌──────────────┐      ┌─────────────────────────┐
│ User Query   │ ───> │ Similarity Search (Top-k)│
└──────────────┘      └─────────────────────────┘
                               │
                               ▼
                      ┌─────────────────────────┐
                      │ Context-Injected Prompt │
                      └─────────────────────────┘
                               │
                               ▼
                      ┌─────────────────────────┐
                      │ Google Gemini 2.0 Flash │
                      └─────────────────────────┘
                               │
                               ▼
                      ┌─────────────────────────┐
                      │ Streamlit Chat UI / API │
                      └─────────────────────────┘
```

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Language** | Python 3.10+ | Core development |
| **LLM** | Google Gemini 2.0 Flash | Natural language generation & reasoning |
| **Orchestration** | LangChain / LCEL | RAG pipelines, prompt templates, chains |
| **Embeddings** | HuggingFace `all-MiniLM-L6-v2` | Dense semantic vector representations |
| **Vector DB** | ChromaDB / AstraDB | Persistent similarity vector search |
| **Backend** | FastAPI + Uvicorn | Asynchronous REST API service |
| **Frontend** | Streamlit | Chat user interface with custom NITA styling |
| **Data Ingestion**| BeautifulSoup4, pdfplumber, pypdf | Web scraping and PDF extraction |

---

## 📁 Repository Structure

```text
NITAverse/
├── backend/                  # FastAPI REST backend & RAG pipeline
│   ├── main.py               # API endpoints & LangChain query chain
│   └── check_db.py           # Vector database diagnostics & verification
├── frontend/                 # Interactive user interface
│   ├── app.py                # Streamlit web app with custom institute styling
│   └── logo/                 # Institutional assets & badges
├── scripts/                  # Data collection & preprocessing pipeline
│   ├── web_url_crawler.py    # Recursive web crawler for nita.ac.in
│   ├── web_pdf_link_crawler.py # Discovery script for notice PDFs
│   ├── pdf_downloader.py     # Automated batch PDF downloader
│   ├── pdf_link_correcter.py # URL normalizer & dead-link handler
│   ├── file_cleaner_script.py# Text sanitization & boilerplate removal
│   ├── pdf_metadata_gen.py   # Schema generator for notices
│   └── processor.py          # Unified chunking, embedding & vector indexing
├── data/                     # Data stores (sample URLs & metadata schemas)
├── requirements.txt          # Production dependencies
├── .env.example              # Environment variables template
└── README.md                 # Project documentation
```

---

## 🚀 Quickstart Guide

### 1. Clone the Repository
```bash
git clone https://github.com/ayushhh-here/NITAverse.git
cd NITAverse
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv

# Windows
.\venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Copy `.env.example` to `.env` and insert your Google Gemini API key:
```bash
cp .env.example .env
```
Edit `.env`:
```ini
GOOGLE_API_KEY=your_gemini_api_key_here
```

### 5. Run the Application

**Option A: Streamlit Web UI**
```bash
streamlit run frontend/app.py
```

**Option B: FastAPI Backend Service**
```bash
uvicorn backend.main:app --reload --port 8000
```
Interactive API documentation will be available at `http://localhost:8000/docs`.

---

## 🗺️ Roadmap & Development Plan

- [x] **Day 1**: Project architecture, repository design & environment setup
- [ ] **Day 2**: Web crawlers & portal URL discovery scripts
- [ ] **Day 3**: PDF batch downloader & link correction utilities
- [ ] **Day 4**: PDF text extraction and tabular parsing engine
- [ ] **Day 5**: Text normalization and boilerplate removal pipeline
- [ ] **Day 6**: Metadata extraction & structured JSON unification
- [ ] **Day 7**: Pipeline validation & test benchmarks
- [ ] **Day 8**: Document chunking strategy (`RecursiveCharacterTextSplitter`)
- [ ] **Day 9**: Embedding generation & ChromaDB vector indexing
- [ ] **Day 10**: Context-grounded Gemini 2.0 Flash RAG chain
- [ ] **Day 11**: FastAPI backend service implementation
- [ ] **Day 12**: Streamlit web interface with custom NITA branding
- [ ] **Day 13**: Fallback handling & query response caching
- [ ] **Day 14**: End-to-end integration, demo, and deployment

---

## 👤 Author

**Ayush**
- GitHub: [@ayushhh-here](https://github.com/ayushhh-here)
- Project: [NITAverse](https://github.com/ayushhh-here/NITAverse)

---

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
