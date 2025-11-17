# AI Emergency Response & Safety Alert System
_A smart system that analyzes text and audio to detect emergencies (fire, accident, medical, SOS)_

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/kotaRamyapriya/kotaramyapriya-ai-emergency-system?style=social)](https://github.com/kotaRamyapriya/kotaramyapriya-ai-emergency-system/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/kotaRamyapriya/kotaramyapriya-ai-emergency-system?style=social)](https://github.com/kotaRamyapriya/kotaramyapriya-ai-emergency-system/network)
[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![Docker Pulls](https://img.shields.io/docker/pulls/kotaramyapriya/ai-emergency-system-image)](https://hub.docker.com/)

---

## Demo
![AI Emergency System Demo](assets/demo.gif)  
*Replace `assets/demo.gif` with your actual GIF showing frontend UI and alerts.*

---

## Motivation
In critical situations, timely alerts can save lives. Many people may be unable to call for help directly due to injury, panic, or inaccessibility.  
This system detects emergencies via audio or text input, classifies the type of emergency, and triggers alerts in real time to help responders act faster.

---

## Features
- Real-time audio capture and transcription  
- Keyword/phrase classification: fire, accident, medical, SOS  
- Web-based UI with FastAPI backend  
- Containerized deployment with Docker and Docker Compose  
- Easy local setup and testing  

---

## Tech Stack
- **Backend:** FastAPI (Python)  
- **Frontend:** HTML, CSS, JavaScript  
- **Speech Recognition:** Web Speech API / SpeechRecognition Python library  
- **Containerization:** Docker, Docker Compose  

---

## Architecture
**User (Browser) → Frontend UI → Backend API → Classifier → Alert/Response**

- Frontend captures audio or text input from the user.  
- Backend receives input and passes it to a simple classifier (keyword-based or ML model).  
- System returns the classified emergency type and triggers the appropriate alert/log.  

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

# Build and start containers
docker-compose up --build
Access the system
Backend: http://localhost:8000

Frontend: http://localhost:8080

Usage / Testing
Open the frontend in a browser (http://localhost:8080)

Click Start Listening for audio input or type a text message

Examples of input:

"fire fire"

"help accident"

"medical emergency"

The system shows the detected emergency type in the UI

Alerts are logged in the backend console

Folder Structure
bash
Copy code
/backend      — FastAPI backend application
/frontend     — Static HTML, CSS, JS files
docker-compose.yml
README.md
LICENSE
/assets      — Screenshots or demo GIFs
Model / Data
Current system uses keyword matching for emergency classification

Future versions may integrate machine learning models for better audio/text detection

No external datasets are required for current implementation

Contributing
Contributions are welcome! Please follow these steps:

Fork the repository

Create a feature branch

Make your changes

Submit a pull request with a clear description

See CONTRIBUTING.md for detailed instructions.

Roadmap / Future Enhancements
Integrate ML models for improved emergency detection

Multi-language support

SMS or push notifications for emergencies

Advanced audio classification and alert prioritization

License
This project is licensed under the MIT License.
MIT © 2025 Kota Ramyapriya

yaml
Copy code
