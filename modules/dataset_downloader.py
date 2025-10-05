# modules/dataset_downloader.py
import kagglehub
import os

def download_dataset():
    print("📦 Downloading Mental Health dataset from Kaggle...")

    # This dataset contains labeled mental health text data
    path = kagglehub.dataset_download("reihanenamdari/mental-health-corpus")

    print("✅ Dataset downloaded successfully!")
    print("📂 Path to dataset files:", path)
    return path

if __name__ == "__main__":
    download_dataset()
