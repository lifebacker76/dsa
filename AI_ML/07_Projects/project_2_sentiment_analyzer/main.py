"""
Sentiment Analyzer — NLP with Transformers
==========================================

Classify movie reviews as positive or negative.
Baseline: TF-IDF + Logistic Regression
Advanced: Fine-tuned BERT

Usage:
    python main.py
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, classification_report
)
from sklearn.model_selection import train_test_split


# =============================================================================
# Step 1: Data Loading & Exploration
# =============================================================================

def load_data():
    """Load the IMDB dataset.

    Returns:
        pd.DataFrame: DataFrame with 'text' and 'label' columns.
            label: 0 = negative, 1 = positive

    Options:
        - HuggingFace: datasets.load_dataset("imdb")
        - Manual CSV download from Kaggle
    """
    pass


def explore_data(df):
    """Explore the dataset — class distribution, text lengths, samples.

    Args:
        df (pd.DataFrame): Dataset with 'text' and 'label' columns.

    Prints/Plots:
        - Class distribution (value_counts)
        - Histogram of review lengths (word count)
        - Sample reviews from each class
    """
    pass


# =============================================================================
# Step 2: Text Preprocessing
# =============================================================================

def preprocess_text(text):
    """Clean a single text review.

    Args:
        text (str): Raw review text.

    Returns:
        str: Cleaned text.

    Steps:
        - Lowercase
        - Remove HTML tags (<br />, etc.)
        - Remove URLs
        - Remove special characters (keep letters, numbers, spaces)
        - Strip extra whitespace
    """
    pass


def preprocess_dataset(df):
    """Apply preprocessing to all reviews in the dataset.

    Args:
        df (pd.DataFrame): Dataset with 'text' column.

    Returns:
        pd.DataFrame: Dataset with cleaned 'text' column.
    """
    pass


# =============================================================================
# Step 3: Baseline — TF-IDF + Logistic Regression
# =============================================================================

def train_baseline(X_train, y_train, max_features=10000, ngram_range=(1, 2)):
    """Train TF-IDF + Logistic Regression baseline.

    Args:
        X_train (pd.Series): Training review texts.
        y_train (pd.Series): Training labels.
        max_features (int): Max vocabulary size for TF-IDF.
        ngram_range (tuple): N-gram range for TF-IDF.

    Returns:
        tuple: (vectorizer, model) — fitted TfidfVectorizer and LogisticRegression.
    """
    pass


def evaluate_model(model, X_test_vec, y_test, model_name="Model"):
    """Evaluate a classification model and print metrics.

    Args:
        model: Trained classifier.
        X_test_vec: Vectorized test features.
        y_test (pd.Series): True labels.
        model_name (str): Name for display.

    Returns:
        dict: {"accuracy": ..., "precision": ..., "recall": ..., "f1": ...}

    Prints:
        - Classification report
        - Confusion matrix
    """
    pass


# =============================================================================
# Step 4: BERT Fine-Tuning
# =============================================================================

def tokenize_for_bert(texts, tokenizer, max_length=256):
    """Tokenize texts for BERT input.

    Args:
        texts (list[str]): List of review texts.
        tokenizer: HuggingFace BertTokenizer.
        max_length (int): Maximum sequence length.

    Returns:
        dict: {"input_ids": tensor, "attention_mask": tensor}
    """
    pass


def create_dataloader(encodings, labels, batch_size=16, shuffle=True):
    """Create a PyTorch DataLoader from tokenized data.

    Args:
        encodings (dict): Tokenized inputs.
        labels (list or np.ndarray): Labels.
        batch_size (int): Batch size.
        shuffle (bool): Whether to shuffle.

    Returns:
        torch.utils.data.DataLoader
    """
    pass


def train_bert(model, train_loader, val_loader, epochs=3, lr=2e-5):
    """Fine-tune BERT for sentiment classification.

    Args:
        model: BertForSequenceClassification.
        train_loader: Training DataLoader.
        val_loader: Validation DataLoader.
        epochs (int): Number of training epochs.
        lr (float): Learning rate.

    Returns:
        dict: Training history {"train_loss": [...], "val_loss": [...], "val_acc": [...]}
    """
    pass


def evaluate_bert(model, test_loader):
    """Evaluate fine-tuned BERT on test data.

    Args:
        model: Fine-tuned BERT model.
        test_loader: Test DataLoader.

    Returns:
        dict: {"accuracy": ..., "precision": ..., "recall": ..., "f1": ...}
    """
    pass


# =============================================================================
# Step 5: Comparison & Analysis
# =============================================================================

def compare_models(baseline_metrics, bert_metrics):
    """Create a comparison table of baseline vs BERT.

    Args:
        baseline_metrics (dict): Metrics from TF-IDF + LogReg.
        bert_metrics (dict): Metrics from fine-tuned BERT.

    Returns:
        pd.DataFrame: Side-by-side comparison.
    """
    pass


def error_analysis(texts, true_labels, baseline_preds, bert_preds, n=10):
    """Analyze examples where models disagree or both fail.

    Args:
        texts (list[str]): Review texts.
        true_labels (list[int]): True labels.
        baseline_preds (list[int]): Baseline predictions.
        bert_preds (list[int]): BERT predictions.
        n (int): Number of examples to show.
    """
    pass


# =============================================================================
# Step 6: Prediction
# =============================================================================

def predict_sentiment(text, vectorizer=None, model=None):
    """Predict sentiment for a single review.

    Args:
        text (str): Review text.
        vectorizer: Fitted TfidfVectorizer (for baseline).
        model: Trained model.

    Returns:
        dict: {"sentiment": "positive"/"negative", "confidence": float}
    """
    pass


# =============================================================================
# Main Pipeline
# =============================================================================

def main():
    """Run the full sentiment analysis pipeline.

    Steps:
        1. Load and explore data
        2. Preprocess text
        3. Train TF-IDF + LogReg baseline
        4. Fine-tune BERT
        5. Compare models
        6. Error analysis
    """
    print("=" * 60)
    print("Sentiment Analyzer — NLP Pipeline")
    print("=" * 60)

    # Step 1: Load data
    print("\n📊 Step 1: Loading data...")
    # df = load_data()
    # explore_data(df)

    # Step 2: Preprocess
    print("\n🧹 Step 2: Preprocessing text...")
    # df = preprocess_dataset(df)
    # X_train, X_test, y_train, y_test = train_test_split(...)

    # Step 3: Baseline
    print("\n📏 Step 3: Training baseline (TF-IDF + LogReg)...")
    # vectorizer, lr_model = train_baseline(X_train, y_train)
    # baseline_metrics = evaluate_model(lr_model, X_test_vec, y_test, "Baseline")

    # Step 4: BERT
    print("\n🤖 Step 4: Fine-tuning BERT...")
    # (see notebook for GPU-based training)

    # Step 5: Compare
    print("\n📊 Step 5: Comparing models...")
    # comparison = compare_models(baseline_metrics, bert_metrics)
    # print(comparison)

    # Step 6: Test prediction
    print("\n🔮 Step 6: Test prediction...")
    # result = predict_sentiment("This movie was absolutely fantastic!", vectorizer, lr_model)
    # print(result)

    print("\n✅ Pipeline complete!")


if __name__ == "__main__":
    main()
