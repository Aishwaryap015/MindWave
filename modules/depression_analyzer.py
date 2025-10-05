# modules/depression_analyzer.py
from modules.mood_model import load_model
import numpy as np

class DepressionAnalyzer:
    def __init__(self):
        self.model, self.vectorizer = load_model()
        if self.model is None or self.vectorizer is None:
            raise ValueError("Mood model not loaded. Run `python3 -m modules.mood_model` first.")

        self.labels = list(self.model.classes_)
        print(f"🧩 Model labels detected: {self.labels}")

        # Start with a blank map — will always auto-correct:
        self.label_map = {}
        self._auto_fix_label_map()

    def _auto_fix_label_map(self):
        """Test model predictions on known happy/sad to determine mapping dynamically."""
        happy_vec = self.vectorizer.transform(["I am very happy"])
        sad_vec = self.vectorizer.transform(["I am very sad"])

        happy_pred = int(self.model.predict(happy_vec)[0])
        sad_pred = int(self.model.predict(sad_vec)[0])

        # Now set mapping dynamically:
        self.label_map[happy_pred] = "happiness"
        self.label_map[sad_pred] = "sadness"

        print(f"✅ Dynamic label mapping built: {self.label_map}")

    def analyze(self, text):
        """Analyze user text and return (emotion, confidence)."""
        if not text.strip():
            return "neutral", 0.0

        X = self.vectorizer.transform([text])
        probs = self.model.predict_proba(X)[0]
        labels = self.model.classes_

        idx = int(np.argmax(probs))
        raw_label = int(labels[idx])
        confidence = float(probs[idx])

        emotion = self.label_map.get(raw_label, f"label_{raw_label}")
        return emotion, confidence
