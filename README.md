🧠 MindTrack v4.1
An Offline ML-Powered Mental Wellness Assistant

Author: Aishwarya Priyadarshni
Email: pdarshniaishwarya@gmail.com
License: MIT
Version: 4.1

🌿 Overview

MindTrack is an intelligent, offline mental wellness assistant that uses machine learning to analyze emotions from text or speech.
It offers a calm, voice-guided experience to help you reflect, track your moods, and stay motivated every day.

This project runs completely offline, making it both private and secure.

✨ Features: 

| Feature                 | Description                                                              |
| ----------------------- | ------------------------------------------------------------------------ |
| 🎯 **Emotion Analysis** | Analyze your mood by typing or speaking your feelings.                   |
| 📜 **Mood History**     | Automatically saves your previous emotions in a local CSV file.          |
| 📈 **Mood Chart**       | Visualize emotional trends over time using interactive charts.           |
| 💖 **Daily Motivation** | Get uplifting motivational quotes for your mental wellness.              |
| 🎧 **Voice Assistance** | Female AI voice reads menus and responses aloud for natural interaction. |


⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/yourusername/MindTrack.git
cd MindTrack

2️⃣ Create a virtual environment
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Train or load the emotion model

To train (only needed once):
python3 -m modules.mood_model

This will train the model on the Kaggle Emotions Dataset and save it as:
modules/mood_model.pkl

🧩 Project Structure

MindTrack/
├── main.py                        # Main program (UI + logic)
├── modules/
│   ├── __init__.py
│   └── mood_model.py              # Machine learning model trainer/loader
├── mood_history.csv               # Auto-generated user mood log
├── requirements.txt               # All required dependencies
└── README.md                      # Project documentation

🖥️ Usage

Run the main app: python3 main.py

Then follow the voice-guided menu:

🌸 Main Menu:
1️⃣ Analyze Emotion
2️⃣ Show Mood History
3️⃣ View Mood Chart
4️⃣ Daily Motivation
5️⃣ Exit

You can either type or speak your feelings.
All results will be saved automatically to mood_history.csv.

📊 Example Outputs

Detected Emotion:
💬 Detected Emotion: joy
✅ Saved to mood history.


Mood History Sample:
       Date     Emotion                     Text
2025-10-05       joy          I feel really happy today!
2025-10-06   sadness          I miss my old friends.

Chart Example:
Displays a time-series trend of emotions.

💬 Dependencies

| Library              | Purpose                        |
| -------------------- | ------------------------------ |
| `pandas`             | Handle mood history storage    |
| `matplotlib`         | Create emotion trend charts    |
| `speech_recognition` | Speech-to-text input           |
| `pyttsx3`            | Text-to-speech voice assistant |
| `scikit-learn`       | ML model for emotion detection |


Install all from requirements.txt or manually:
pip install pandas matplotlib SpeechRecognition pyttsx3 scikit-learn

💡 Future Enhancements

🧘 Add breathing and mindfulness exercises

☁️ Optional cloud sync for mood history

📱 GUI-based dashboard using Tkinter or React


📫 Contact

Author: Aishwarya Priyadarshni
📧 pdarshniaishwarya@gmail.com



