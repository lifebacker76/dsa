# 🎭 Project 2: Sentiment Analyzer

**NLP with Transformers**

| | |
|---|---|
| **Difficulty** | ⭐⭐⭐ Intermediate+ |
| **Time Estimate** | 10–15 hours |
| **Prerequisites** | Classical ML, NLP Fundamentals, Deep Learning basics |

---

## Overview

Build a sentiment analysis system that classifies movie reviews as **positive** or **negative**. Start with a classical baseline (TF-IDF + Logistic Regression), then level up to a fine-tuned BERT model. Finally, serve your model through a simple REST API.

**Goal:** Classify movie review text as positive or negative sentiment.

---

## Dataset

- **IMDB Reviews** — 50,000 labeled movie reviews (25k train, 25k test)
- Load via HuggingFace: `datasets.load_dataset("imdb")`
- Or download manually from [Kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)

---

## Steps

### Step 1: Data Exploration
- Load and inspect the dataset
- Check class balance (positive vs negative counts)
- Explore text lengths — histogram of review word counts
- Sample and read a few reviews from each class
- Word cloud for positive vs negative reviews (optional)

### Step 2: Baseline — TF-IDF + Logistic Regression
- Preprocess text: lowercase, remove HTML tags, strip punctuation
- Vectorize with `TfidfVectorizer` (experiment with n-grams, max_features)
- Train Logistic Regression
- Evaluate: accuracy, precision, recall, F1, confusion matrix
- This is your baseline — any fancy model must beat it

### Step 3: Fine-Tune a Pretrained BERT Model
- Tokenize reviews with `BertTokenizer` (handle max_length, padding, truncation)
- Create a PyTorch Dataset and DataLoader
- Load `bert-base-uncased` with `BertForSequenceClassification`
- Fine-tune for 2–3 epochs with AdamW optimizer and linear scheduler
- Track training/validation loss per epoch

### Step 4: Compare Baseline vs BERT
- Create a comparison table:
  | Model | Accuracy | F1 | Training Time |
  |-------|----------|-----|--------------|
  | TF-IDF + LogReg | ? | ? | ? |
  | Fine-tuned BERT | ? | ? | ? |
- Analyze: where does BERT do better? Where does it fail?
- Look at examples both models get wrong

### Step 5: Build a Simple API
- Create a FastAPI app that accepts review text and returns sentiment
- Endpoint: `POST /predict` with JSON body `{"text": "..."}`
- Returns: `{"sentiment": "positive", "confidence": 0.92}`
- Test with `curl` or `requests`

---

## What You'll Learn

| Skill | Notebook Topic |
|-------|---------------|
| Text preprocessing | `09_NLP/` |
| TF-IDF vectorization | `09_NLP/` |
| Logistic Regression for NLP | `06_Classical_ML/` |
| Transformers & BERT | `09_NLP/`, `08_Deep_Learning/` |
| Fine-tuning with HuggingFace | `09_NLP/` |
| PyTorch training loop | `08_Deep_Learning/` |
| FastAPI basics | `12_MLOps/` |

---

## Deliverables Checklist

- [ ] EDA notebook with text analysis and visualizations
- [ ] TF-IDF + Logistic Regression baseline with metrics
- [ ] Fine-tuned BERT model with training curves
- [ ] Side-by-side comparison table
- [ ] Error analysis — examples both models get wrong
- [ ] FastAPI endpoint that returns predictions
- [ ] Clean `main.py` with modular functions
- [ ] Brief write-up: baseline vs BERT trade-offs

---

## Starter Code

See [`main.py`](main.py) for the project skeleton.

```
project_2_sentiment_analyzer/
├── README.md
├── main.py              # Main pipeline script
├── notebook.ipynb       # EDA and experimentation (create this)
├── api.py               # FastAPI app (create this)
├── models/              # Saved models (create this)
└── data/                # Downloaded data (create this)
```
