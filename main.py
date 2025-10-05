import os
import pickle
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import speech_recognition as sr
import pyttsx3
from modules import mood_model

# ----------------------- INITIAL SETUP -----------------------
print("\n🌿 MindTrack v4.1 — ML-Powered Mental Wellness Assistant (Offline)")

# Load trained model
try:
    model, vectorizer, labels = mood_model.load_model()
    print("✅ Model loaded successfully.\n")
except Exception as e:
    print(f"❌ Model load failed: {e}")
    exit()

# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 165)
voices = engine.getProperty('voices')
# Set to female voice
for voice in voices:
    if "female" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

def speak(text):
    engine.say(text)
    engine.runAndWait()

# CSV file for history
HISTORY_FILE = "mood_history.csv"

# ----------------------- FUNCTIONS -----------------------
def analyze_mood():
    speak("Would you like to type or speak your feelings?")
    print("\n🎧 Choose Input Mode:")
    print("1️⃣ Type your feelings")
    print("2️⃣ Speak your feelings")
    choice = input("👉 Enter choice (1 or 2): ").strip()

    if choice == "2":
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("🎙️ Speak now...")
            audio = recognizer.listen(source)
        try:
            user_text = recognizer.recognize_google(audio)
            print(f"🗣️ You said: {user_text}")
        except sr.UnknownValueError:
            print("⚠️ Sorry, I couldn’t understand your voice.")
            speak("Sorry, I could not understand that.")
            return
    else:
        user_text = input("✍️ Type how you feel: ")

    if not user_text.strip():
        print("⚠️ No input provided.")
        return

    # Vectorize and predict
    text_vec = vectorizer.transform([user_text])
    pred = model.predict(text_vec)[0]

    # Convert prediction to readable label
    if isinstance(pred, (list, tuple, set)):
        pred = list(pred)[0]
    if hasattr(pred, 'item'):
        pred = pred.item()

    emotion = str(pred)
    print(f"💬 Detected Emotion: {emotion}")
    speak(f"You seem to be feeling {emotion}")

    # Save to history
    save_history(emotion, user_text)
    print("✅ Saved to mood history.\n")

def save_history(emotion, text):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    entry = pd.DataFrame([[date, emotion, text]], columns=["Date", "Emotion", "Text"])
    if os.path.exists(HISTORY_FILE):
        old = pd.read_csv(HISTORY_FILE)
        df = pd.concat([old, entry], ignore_index=True)
    else:
        df = entry
    df.to_csv(HISTORY_FILE, index=False)

def show_history():
    if not os.path.exists(HISTORY_FILE):
        print("⚠️ No mood history found yet.")
        speak("You don't have any mood history yet.")
        return
    df = pd.read_csv(HISTORY_FILE)
    print("\n📜 Mood History:\n")
    print(df.tail(10).to_string(index=False))
    speak("Here is your recent mood history.")

def show_chart():
    if not os.path.exists(HISTORY_FILE):
        print("⚠️ No mood history to chart.")
        speak("You don't have enough data for a chart yet.")
        return

    df = pd.read_csv(HISTORY_FILE)
    if "Date" not in df.columns or "Emotion" not in df.columns:
        print("⚠️ CSV file format issue. Expected columns: Date, Emotion, Text")
        return

    df["Date"] = pd.to_datetime(df["Date"])
    trend = df.groupby(["Date", "Emotion"]).size().unstack(fill_value=0)
    trend.plot(kind="line", marker="o", figsize=(10, 5))
    plt.title("📈 Mood Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Emotion Count")
    plt.legend(title="Emotion", bbox_to_anchor=(1.05, 1))
    plt.tight_layout()
    plt.show()
    speak("Here is your emotional trend over time.")

def daily_motivation():
    quotes = [
        "Every day may not be good, but there’s something good in every day.",
        "You are stronger than you think.",
        "Small progress is still progress.",
        "Breathe. You’re doing just fine.",
        "Happiness often sneaks in through doors you didn’t know you left open."
    ]
    import random
    quote = random.choice(quotes)
    print(f"\n💖 Motivation of the Day:\n“{quote}”\n")
    speak(f"Here is your motivation of the day. {quote}")

# ----------------------- MAIN MENU -----------------------
while True:
    print("\n🌸 Main Menu:")
    print("1️⃣ Analyze Emotion")
    print("2️⃣ Show Mood History")
    print("3️⃣ View Mood Chart")
    print("4️⃣ Daily Motivation")
    print("5️⃣ Exit")

    speak("Please choose an option. One, analyze emotion. Two, show history. Three, view chart. Four, daily motivation. Or five, exit.")
    choice = input("👉 Enter your choice (1-5): ").strip()

    if choice == "1":
        analyze_mood()
    elif choice == "2":
        show_history()
    elif choice == "3":
        show_chart()
    elif choice == "4":
        daily_motivation()
    elif choice == "5":
        print("👋 Goodbye! Take care of yourself.")
        speak("Goodbye. Take care of yourself.")
        break
    else:
        print("⚠️ Invalid option, please try again.")
        speak("Invalid choice. Please try again.")
