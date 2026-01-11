# 🚀 Agentic AI Blog Generator

An AI-powered blog generation backend built with **FastAPI** and **LangGraph** that automates blog creation using agentic workflows and Large Language Models (LLMs).

This project demonstrates how to design **modular, production-ready GenAI systems** with clean architecture, scalable AI pipelines, and modern deployment practices.

---

## ✨ Features

- 🧠 Agentic AI workflow using **LangGraph**
- ⚡ High-performance API built with **FastAPI**
- ✍️ Automated blog generation:
  - Title creation
  - Content generation
- 🧩 Clean modular architecture:
  - graphs / nodes / states / llms
- 🔐 Secure environment variable handling
- 📑 Interactive API docs with **Swagger UI**
- ☁️ Ready for deployment on **Railway, Render, Fly.io**

---

## 🏗️ Tech Stack

- **Backend:** FastAPI  
- **AI Orchestration:** LangGraph  
- **LLM Integration:** LangChain + OpenAI  
- **Server:** Uvicorn  
- **Config:** python-dotenv  
- **Deployment:** Railway / Render  

---

## 📁 Project Structure

├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
└── src/
├── init.py
├── graphs/
│ ├── init.py
│ └── graph_builder.py
│
├── llms/
│ ├── init.py
│ └── openaillm.py
│
├── nodes/
│ ├── init.py
│ └── blog_node.py
│
└── states/
├── init.py
└── blogstate.py


---

# 🛠️ Local Setup Guide

Follow these steps to run the project on your system.

---

## 1️⃣ Clone the repository

```bash
git clone https://github.com/bahirsanket9-hub/agentic-ai-blog-generator.git
cd ai-blog-generator

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

Create .env file
OPENAI_API_KEY=your_api_key_here

Run the application
uvicorn app:app --reload

Open API documentation:
http://127.0.0.1:8000/docs


