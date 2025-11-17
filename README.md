# AI Emergency Response & Safety Alert System  
_A smart system that analyzes text + audio to detect emergencies (fire, accident, medical, SOS)_

## Motivation  
In critical situations … (why this exists) …

## Features  
- Real‑time audio capture and transcription  
- Keyword/phrase classification (fire, accident, medical, SOS)  
- Web UI + API backend  
- Containerised with Docker for easy deployment  

## Tech Stack  
- Backend: FastAPI (Python)  
- Frontend: Vanilla HTML/CSS/JavaScript  
- Speech Recognition: Web Speech API or SpeechRecognition Python library  
- Containerisation: Docker, Docker Compose  

## Architecture  
_(Insert diagram or describe flow)_  
Frontend ↔ Backend API ↔ Model/Classifier → Alert  

## Installation  
### Prerequisites  
- Docker (v20.x)  
- Docker Compose (v2.x)  
### Run  
docker-compose up --build

markdown
Copy code
- Backend: http://localhost:8000  
- Frontend: http://localhost:8080  

## Usage  
1. In web browser click “Start Listening”  
2. Speak a phrase: “fire fire”, “help accident”, “medical emergency”  
3. The system classifies and … (show expected result)  

## Folder Structure  
/backend — FastAPI app code
/frontend — static HTML/JS/CSS
docker-compose.yml
README.md
LICENSE

markdown
Copy code

## Model / Data  
Describe how classification works, model used (if any).  

## Future Enhancements  
- Add multi‑language support  
- Integrate SMS or WhatsApp alerts  
- Train a deep learning model for better accuracy  
- Mobile‑friendly UI  

## Contributing  
Contributions welcome! Please open an issue or pull request.  

## License  
MIT © 2025 Kota Ramyapriya  
