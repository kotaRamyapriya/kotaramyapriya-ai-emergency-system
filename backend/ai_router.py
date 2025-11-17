from audio_transcriber import transcribe_audio

# TEXT ANALYSIS USING SIMPLE RULE-BASED LOGIC
def analyze_text(text: str):
    text = text.lower()

    if "fire" in text:
        return "Possible fire emergency detected"
    if "accident" in text or "injured" in text:
        return "Possible accident or injury"
    if "help" in text or "emergency" in text:
        return "User requested urgent help"

    return "No major emergency detected"

# AUDIO → TEXT → ANALYSIS
async def analyze_audio(file):
    transcription = await transcribe_audio(file)
    return transcription
