import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
import pandas as pd

MODEL_PATH = os.path.join(os.path.dirname(__file__), "mood_model.pkl")

# --------------------------------
# Train Model (run: python3 -m modules.mood_model)
# --------------------------------
def train_model():
    print("🧠 Training Mood Model using Kaggle Emotions Dataset...")

    dataset_dir = os.path.expanduser("~/.kaggle/emotions")
    train_path = os.path.join(dataset_dir, "train.txt")
    val_path = os.path.join(dataset_dir, "val.txt")

    if not os.path.exists(train_path):
        raise FileNotFoundError("❌ Emotions dataset not found. Please download it first.")

    train_df = pd.read_csv(train_path, sep=";", names=["text", "emotion"])
    val_df = pd.read_csv(val_path, sep=";", names=["text", "emotion"])

    X_train, y_train = train_df["text"], train_df["emotion"]
    X_val, y_val = val_df["text"], val_df["emotion"]

    vectorizer = TfidfVectorizer(max_features=5000, stop_words="english")
    X_train_vec = vectorizer.fit_transform(X_train)
    X_val_vec = vectorizer.transform(X_val)

    model = MultinomialNB()
    model.fit(X_train_vec, y_train)
    preds = model.predict(X_val_vec)

    acc = accuracy_score(y_val, preds)
    print(f"🎯 Accuracy: {acc:.3f}\n")
    print("📋 Classification Report:\n", classification_report(y_val, preds))

    with open(MODEL_PATH, "wb") as f:
        pickle.dump({"model": model, "vectorizer": vectorizer, "labels": model.classes_}, f)

    print(f"\n💾 Model saved at: {MODEL_PATH}")


# --------------------------------
# Load Model
# --------------------------------
def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("❌ Model not found! Please train it first using: python3 -m modules.mood_model")

    with open(MODEL_PATH, "rb") as f:
        data = pickle.load(f)

    model = data["model"]
    vectorizer = data["vectorizer"]
    labels = list(data["labels"])

    return model, vectorizer, labels


if __name__ == "__main__":
    train_model()
