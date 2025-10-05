import pyttsx3

class VoiceManager:
    def __init__(self, language='english', gender='female'):
        self.engine = pyttsx3.init()

        # Normalize user input
        language = language.lower().strip()
        gender = gender.lower().strip()

        # Select appropriate voice
        self.voice_id = self.select_voice(language, gender)
        self.engine.setProperty('voice', self.voice_id)
        self.engine.setProperty('rate', 175)

        print(f"✅ Using {language.capitalize()} {gender.capitalize()} voice → {self.voice_id}")

    def select_voice(self, language, gender):
        voices = self.engine.getProperty('voices')

        # Map language to espeak voice codes
        lang_map = {
            'english': 'en-in',  # Indian English
            'hindi': 'hi'        # Hindi
        }

        selected_lang = lang_map.get(language, 'en-in')
        gender_keyword = 'female' if gender == 'female' else 'male'

        # Try to find the closest matching voice
        for v in voices:
            name = v.name.lower()
            lang_code = (
                v.languages[0].decode('utf-8') if isinstance(v.languages[0], bytes)
                else str(v.languages[0])
            ).lower()

            if selected_lang in lang_code or selected_lang in name:
                if gender_keyword in name:
                    return v.id

        # Fallback: pick first voice that matches language
        for v in voices:
            if selected_lang in v.id.lower():
                return v.id

        # Last fallback
        return voices[0].id

    def speak(self, text):
        """Speak the given text using current voice"""
        self.engine.say(text)
        self.engine.runAndWait()
