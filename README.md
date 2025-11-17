# AI Emergency Response & Safety Alert System  
_A smart system that analyzes text and audio to detect emergencies (fire, accident, medical, SOS)_

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## Motivation  
In critical situations, timely alerts can save lives. Many people may be unable to call for help directly due to injury, panic, or inaccessibility.  
This system detects emergencies via audio or text input, classifies the type of emergency, and triggers alerts in real time, helping responders act faster.

---

## Features  
- Real-time audio capture and transcription  
- Keyword/phrase classification: fire, accident, medical, SOS  
- Web-based UI with FastAPI backend  
- Containerized deployment with Docker and Docker Compose  
- Easy setup and run locally  

---

## Tech Stack  
- **Backend:** FastAPI (Python)  
- **Frontend:** Vanilla HTML/CSS/JavaScript  
- **Speech Recognition:** Web Speech API / SpeechRecognition Python library  
- **Containerization:** Docker, Docker Compose  

---

## Architecture  
User (Browser) → Frontend UI → Backend API → Classifier → Alert/Response

yaml
Copy code
- The frontend captures audio or text input from the user.  
- The backend receives input and passes it to a simple classifier (keyword-based or ML model).  
- The system returns the classified emergency type and triggers the appropriate alert/log.

---

## Installation  

### Prerequisites  
- Docker (v20.x or above)  
- Docker Compose (v2.x or above)  

### Run the system  
```bash
# Clone the repository
git clone https://github.com/kotaRamyapriya/kotaramyapriya-ai-emergency-system.git
cd kotaramyapriya-ai-emergency-system

# Build and start the containers
docker-compose up --build
Backend: http://localhost:8000

Frontend: http://localhost:8080

Usage
Open the frontend in a browser (http://localhost:8080).

Click Start Listening (for audio input) or type a text message.

Speak or type a phrase such as:

"fire fire"

"help accident"

"medical emergency"

The system classifies the input and displays the detected emergency type in the UI.

Alerts are logged in the backend console.

Folder Structure
text
Copy code
/backend    — FastAPI backend application
/frontend   — Static HTML, CSS, and JavaScript files
docker-compose.yml
README.md
LICENSE
Model / Data
The classification system currently uses keyword matching to detect the type of emergency.

Future versions may integrate machine learning models for more accurate audio/text classification.

No external datasets are required for the current implementation.

Future Enhancements
Add multi-language support for text and audio input

Integrate SMS or WhatsApp alerts

Train a deep learning model for better accuracy and context understanding

Create a mobile-friendly UI for better accessibility

Contributing
Contributions are welcome! Please open an issue or submit a pull request.

Guidelines:

Fork the repository

Make your changes in a feature branch

Submit a PR with a clear description of your changes

License
MIT © 2025 Kota Ramyapriya

yaml
Copy code

---

This version:  
- Fixes all broken code blocks  
- Properly formats commands, file paths, and ports  
- Organizes content clearly with sections, bullet points, and code blocks  
- Ready for **GitHub, recruiters, or collaborators**  

---

If you want, I can **add a small screenshot/GIF section at the top** showing the system in action — it makes your README visually engaging and more professional.  

Do you want me to add that?
