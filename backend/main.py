from fastapi import FastAPI, UploadFile, File
from ai_router import analyze_text, analyze_audio
from incident_classifier import classify_incident
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Emergency Response System",
    description="Analyzes text & audio to detect emergency incidents",
    version="1.0.0"
)

# ✅ Enable CORS so frontend can access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "AI Emergency Response System is running!"}

@app.post("/analyze-text")
async def analyze_text_endpoint(input_text: str):
    ai_result = analyze_text(input_text)
    incident_type = classify_incident(input_text)

    return {
        "input": input_text,
        "ai_analysis": ai_result,
        "incident_type": incident_type
    }

@app.post("/analyze-audio")
async def analyze_audio_endpoint(file: UploadFile = File(...)):
    audio_text = await analyze_audio(file)
    incident_type = classify_incident(audio_text)

    return {
        "transcription": audio_text,
        "incident_type": incident_type
    }

