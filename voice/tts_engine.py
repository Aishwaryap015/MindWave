# voice/tts_engine.py
import pyttsx3

class VoiceManager:
    def __init__(self):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')

        # Try Indian male voice, else first male
        male_voice = next((v for v in voices if "male" in v.name.lower() or "hindi" in v.name.lower()), None)
        self.engine.setProperty('voice', male_voice.id if male_voice else voices[0].id)
        self.engine.setProperty('rate', 170)
        print("🎙️ Using male voice for output.")

    def speak(self, text):
        print(f"AI: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
