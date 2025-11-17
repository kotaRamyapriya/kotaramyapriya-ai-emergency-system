def classify_incident(text: str):
    text = text.lower()

    if "fire" in text or "smoke" in text:
        return "FIRE"
    if "accident" in text or "injury" in text:
        return "ACCIDENT"
    if "unconscious" in text or "not breathing" in text:
        return "MEDICAL"
    if "help" in text or "emergency" in text:
        return "GENERAL EMERGENCY"

    return "UNKNOWN"
