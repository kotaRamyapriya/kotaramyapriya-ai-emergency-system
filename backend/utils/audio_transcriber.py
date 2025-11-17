import speech_recognition as sr

async def transcribe_audio(file):
    recognizer = sr.Recognizer()

    with open("temp_audio.wav", "wb") as buffer:
        buffer.write(await file.read())

    with sr.AudioFile("temp_audio.wav") as source:
        audio = recognizer.record(source)

    try:
        return recognizer.recognize_google(audio)
    except:
        return "Audio not clear"
