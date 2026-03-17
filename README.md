# NLP Question Answering System (FLAN-T5)

## 📌 Project Overview
This project is an NLP-based Question Answering System built using Google's FLAN-T5 model. It takes user input questions and generates meaningful answers using a transformer-based deep learning model integrated with a Flask backend and a modern web frontend.

This project demonstrates real-time NLP inference using a transformer-based generative model integrated into a full-stack web application.

## 🚀 Features
- Ask any general knowledge question and get an instant answer
- Powered by Google's FLAN-T5 pre-trained language model
- Real-time inference using Hugging Face Transformers
- Clean and modern UI
- REST API backend built with Flask
- Runs offline after initial model download

## 🛠 Tech Stack
- Frontend: HTML, CSS, JavaScript
- Backend: Python, Flask
- AI Model: Google FLAN-T5 (HuggingFace Transformers)
- Deep Learning: PyTorch

## 📂 Project Structure
text-to-text/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
└── README.md

## ▶️ Installation and Setup

Step 1 — Clone the repository
git clone https://github.com/Rakhesh143/Text-To-Text1.git
cd Text-To-Text1

Step 2 — Install dependencies
pip install -r requirements.txt

Step 3 — Run the application
python app.py

Open your browser:
http://127.0.0.1:5000

## ⚙️ How It Works
1. User enters a question in the web interface  
2. Frontend sends request to Flask backend  
3. Backend processes input using FLAN-T5 model  
4. Model generates response  
5. Response is displayed on UI  

## 🤖 Model Details
- Model: google/flan-t5-base  
- Library: HuggingFace Transformers  
- Architecture: Text-to-Text Transformer  
- Parameters: ~250M  

## 💡 Example Questions
- What is photosynthesis?  
- Who invented the telephone?  
- What is machine learning?  
- What is the capital of France?  
- Who is the father of computers?  

## 📦 Requirements
flask  
transformers  
torch  
sentencepiece  
flask-cors  

## 📊 Project Status
Completed and Ready for Deployment  

## 🔑 Keywords
NLP, Generative AI, FLAN-T5, Transformers, Flask, REST API, Machine Learning, Deep Learning  

## 🚀 Future Improvements
- Upgrade to FLAN-T5-Large for improved accuracy  
- Add chat history and conversational memory  
- Integrate RAG (Retrieval Augmented Generation)  
- Deploy on cloud (Hugging Face Spaces / Render)  
- Fine-tune model on domain-specific data  

## 👨‍💻 Author
Rakesh Namineni  
LinkedIn: https://www.linkedin.com/in/rakesh-namineni-688062291  
GitHub: https://github.com/Rakhesh143  
