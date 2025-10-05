# modules/preprocess.py
import os
import pandas as pd
from sklearn.model_selection import train_test_split

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_RAW = os.path.join(BASE_DIR, "data", "raw", "mental_corpus.csv")
DATA_PROC = os.path.join(BASE_DIR, "data", "processed")

def preprocess_and_save():
    os.makedirs(DATA_PROC, exist_ok=True)
    print("🧹 Preprocessing dataset...")

    df = pd.read_csv(DATA_RAW)

    # Expecting 'text' and 'label' columns
    df = df[['text', 'label']].dropna()

    # Optional: filter to relevant labels
    valid_labels = ['depression', 'anxiety', 'stress', 'neutral']
    df = df[df['label'].isin(valid_labels)]

    train, test = train_test_split(df, test_size=0.2, stratify=df['label'], random_state=42)

    train.to_csv(os.path.join(DATA_PROC, "train.csv"), index=False)
    test.to_csv(os.path.join(DATA_PROC, "test.csv"), index=False)

    print(f"✅ Preprocessing complete. Train: {len(train)}, Test: {len(test)} samples.")
