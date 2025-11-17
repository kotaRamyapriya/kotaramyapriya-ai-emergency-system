# 🚨 AI Emergency Response & Safety Alert System  
### Team: **RamyapriyaAIHack**

An intelligent cloud-powered system that detects possible emergencies from **text or audio**, classifies the incident using AI, and returns an appropriate safety alert.  
Built for **GHCI 2025 Hackathon – Round 2 Submission**.

---

# 🌟 Features

✔ Detects **Fire / Accident / Medical / SOS**  
✔ Text-based incident classification  
✔ Voice → Text transcription  
✔ AI-powered incident classifier  
✔ Real-time results in the UI  
✔ Dockerized backend + frontend  
✔ FastAPI REST API  
✔ Lightweight prototype  

---

# 🏗 System Architecture

User (Web App)
↓
Frontend (HTML + JavaScript)
↓
FastAPI Backend
↓
AI Incident Classifier
(OpenAI / Azure Cognitive Services)
↓
Emergency Detection Output

yaml
Copy code

---

# 🔧 Tech Stack

### 🖥 Frontend
- HTML  
- CSS  
- JavaScript (Vanilla JS)  
- Web Audio API  

### 🧪 Backend
- FastAPI  
- Python 3.10  
- SpeechRecognition  
- OpenAI or Azure Cognitive Services (configurable)

### 🐳 DevOps
- Docker  
- Docker Compose  

---

# 📁 Project Structure

ai-emergency-system/
│
├── backend
│ ├── main.py
│ ├── ai_router.py
│ ├── incident_classifier.py
│ ├── requirements.txt
│ ├── Dockerfile
│ └── utils
│ └── audio_transcriber.py
│
├── frontend
│ ├── index.html
│ ├── app.js
│ ├── style.css
│
├── docker-compose.yml
└── README.md

yaml
Copy code

---

# ▶️ How to Run the Application

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/kotaRamyapriya/kotaramyapriya-ai-emergency-system
cd kotaramyapriya-ai-emergency-system
2️⃣ Run with Docker Compose
bash
Copy code
docker-compose up --build
3️⃣ Access the App
Service	URL
Backend API	http://localhost:8000
Frontend UI	http://localhost:8080

🤖 API Endpoints
POST /classify
Send text → get emergency type.

Sample Request

json
Copy code
{
  "text": "There is smoke and fire inside the room!"
}
POST /transcribe
Send audio → returns transcription text.

Sample Response

json
Copy code
{
  "transcription": "Please help! Someone fainted!"
}
🔥 AI Components
1️⃣ Incident Classifier
Analyzes user text

Detects: Fire, Accident, Medical, SOS, Non-emergency

Uses OpenAI or Azure AI

2️⃣ Audio Transcriber
Converts recorded audio → text

Passes text to classifier

🔐 Security Measures
API key protection

CORS handling

No user data stored

Optional HTTPS

📈 Future Enhancements
GPS location extraction

Auto alert to emergency contacts

Mobile app version

Multi-language detection

Realtime alert dashboard
docker-compose up --build

