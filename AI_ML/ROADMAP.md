# AI/ML Engineer Learning Roadmap (Python)

> A structured, project-driven path from Python fundamentals to deploying production ML systems.

---

## 📖 How to Use This Repo

1. **Follow the phases in order** — each builds on the previous one
2. **Read the cheatsheet** for each topic first, then work through the notebook
3. **Solve the problems notebook** before moving to the next topic
4. **Build the projects** at the end to solidify everything
5. **Track your progress** in the practice log

---

## 🗺️ Learning Order

| # | Topic | Folder | Est. Time | Prerequisites |
|---|-------|--------|-----------|---------------|
| 01 | Python for Data Science | `01_Python_for_DS/` | 1 week | Basic Python |
| 02 | NumPy Fundamentals | `02_NumPy/` | 1 week | 01 |
| 03 | Pandas & Data Wrangling | `03_Pandas/` | 1.5 weeks | 01, 02 |
| 04 | Data Visualization | `04_Visualization/` | 1 week | 03 |
| 05 | Math for ML | `05_Math_for_ML/` | 2 weeks | 02 |
| 06 | Classical Machine Learning | `06_Classical_ML/` | 3 weeks | 03, 05 |
| 07 | Projects (Classical) | `07_Projects/` | 2 weeks | 06 |
| 08 | Deep Learning Fundamentals | `08_Deep_Learning/` | 3 weeks | 05, 06 |
| 09 | Natural Language Processing | `09_NLP/` | 2 weeks | 06, 08 |
| 10 | Computer Vision | `10_Computer_Vision/` | 2 weeks | 08 |
| 11 | LLMs & Generative AI | `11_LLMs/` | 2 weeks | 09 |
| 12 | MLOps & Deployment | `12_MLOps/` | 2 weeks | 06, 08 |

**Total estimated time: ~22 weeks (5–6 months at ~10 hrs/week)**

---

## 🧩 Phase Breakdown

### Phase 1: Foundations (Weeks 1–4)
> Get fluent in the data science toolkit.

| Topic | What You'll Learn |
|-------|-------------------|
| **Python for Data Science** | List comprehensions, generators, decorators, OOP for ML pipelines |
| **NumPy** | Arrays, broadcasting, vectorized operations, linear algebra ops |
| **Pandas** | DataFrames, groupby, merge, pivot, handling missing data, time series |
| **Visualization** | Matplotlib, Seaborn, Plotly — histograms, scatter plots, heatmaps, subplots |

**Milestone:** Load any CSV, clean it, explore it with stats & plots, export results.

---

### Phase 2: Math & Theory (Weeks 5–6)
> The math that actually matters for ML — no more, no less.

| Topic | What You'll Learn |
|-------|-------------------|
| **Linear Algebra** | Vectors, matrices, dot product, eigenvalues — why they power ML |
| **Calculus** | Derivatives, gradients, chain rule — how models learn |
| **Probability & Statistics** | Distributions, Bayes' theorem, hypothesis testing, maximum likelihood |

**Milestone:** Derive gradient descent by hand. Understand why regularization works.

---

### Phase 3: Classical Machine Learning (Weeks 7–11)
> The bread and butter of applied ML.

| Topic | What You'll Learn |
|-------|-------------------|
| **Supervised Learning** | Linear/Logistic Regression, Decision Trees, Random Forest, SVM, KNN |
| **Unsupervised Learning** | K-Means, DBSCAN, PCA, t-SNE |
| **Model Evaluation** | Cross-validation, confusion matrix, ROC/AUC, precision/recall, bias-variance |
| **Feature Engineering** | Encoding, scaling, feature selection, polynomial features, pipelines |
| **Ensemble Methods** | Bagging, boosting (XGBoost, LightGBM), stacking |

**Milestone:** Build an end-to-end ML pipeline — **Project 1: House Price Predictor**.

---

### Phase 4: Deep Learning & Specializations (Weeks 12–17)
> Neural networks, NLP, and Computer Vision.

| Topic | What You'll Learn |
|-------|-------------------|
| **Neural Network Basics** | Perceptrons, backpropagation, activation functions, optimizers |
| **PyTorch** | Tensors, autograd, nn.Module, DataLoaders, training loops |
| **CNNs** | Convolutions, pooling, architectures (ResNet, VGG), transfer learning |
| **NLP Fundamentals** | Tokenization, TF-IDF, word embeddings, RNNs, attention |
| **Transformers** | Self-attention, BERT, GPT architecture, fine-tuning with HuggingFace |

**Milestones:**
- **Project 2: Sentiment Analyzer** (NLP)
- **Project 3: Image Classifier** (Computer Vision)

---

### Phase 5: LLMs, RAG & Deployment (Weeks 18–22)
> The modern AI stack — from LLMs to production.

| Topic | What You'll Learn |
|-------|-------------------|
| **LLMs in Practice** | Prompt engineering, API usage, tokenization, context windows |
| **RAG Architecture** | Embeddings, vector databases, chunking, retrieval + generation |
| **MLOps** | Model serialization, FastAPI, Docker, monitoring, CI/CD |
| **Cloud Deployment** | AWS/GCP basics, model serving, scaling |

**Milestones:**
- **Project 4: RAG-Powered Chatbot** (LLMs)
- **Project 5: ML Model as an API** (Deployment)

---

## 🛠️ Tools & Libraries

### Core Stack
```bash
# Create a virtual environment first
python -m venv ai_ml_env
source ai_ml_env/bin/activate  # macOS/Linux

# Core data science
pip install numpy pandas matplotlib seaborn scikit-learn jupyter

# Deep learning
pip install torch torchvision torchaudio

# NLP
pip install transformers datasets tokenizers sentencepiece

# LLMs & RAG
pip install openai langchain chromadb faiss-cpu tiktoken

# Deployment
pip install fastapi uvicorn python-multipart joblib

# Utilities
pip install tqdm plotly nbformat ipywidgets
```

### Optional / Advanced
```bash
pip install xgboost lightgbm catboost     # Gradient boosting
pip install optuna                         # Hyperparameter optimization
pip install wandb mlflow                   # Experiment tracking
pip install streamlit gradio              # Quick demos
pip install docker                        # Docker SDK
```

---

## 📅 Suggested Weekly Plan

| Day | Activity | Time |
|-----|----------|------|
| **Mon** | Read cheatsheet + study notebook (theory) | 1.5 hrs |
| **Tue** | Continue notebook + code along | 1.5 hrs |
| **Wed** | Solve problems notebook | 1.5 hrs |
| **Thu** | Solve problems notebook (continued) | 1.5 hrs |
| **Fri** | Work on current project | 2 hrs |
| **Sat** | Project work + review weak spots | 2 hrs |
| **Sun** | Rest / light review / read articles | 0–1 hr |

**Total: ~10–11 hours/week**

---

## 💡 Tips for Learning ML Effectively

### 1. Code First, Theory Second
Don't read 3 textbooks before writing code. Get a model running, *then* understand why it works.

### 2. Build Projects, Not Just Tutorials
Following along ≠ learning. Modify the code. Break it. Fix it. Add features.

### 3. Understand the Data Pipeline
80% of real ML work is data cleaning, feature engineering, and evaluation. Models are the easy part.

### 4. Track Your Experiments
Use notebooks with clear markdown headers. Log hyperparameters and results. Future-you will thank present-you.

### 5. Don't Skip Evaluation Metrics
Accuracy is rarely enough. Learn precision, recall, F1, ROC-AUC, and when each matters.

### 6. Learn to Read Documentation
sklearn docs, PyTorch docs, and HuggingFace docs are your best friends. Practice navigating them.

### 7. Embrace the Debugging
`shape mismatch`, `NaN loss`, `CUDA out of memory` — these errors are your teachers. Read them carefully.

### 8. Learn Git Early
Version your notebooks and code. Commit after each working experiment.

---

## 📚 Resources

### Courses (Free)
- [fast.ai — Practical Deep Learning](https://course.fast.ai/) — Best hands-on DL course
- [Andrew Ng — Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction) — Classic foundations
- [Stanford CS229 — Machine Learning](https://cs229.stanford.edu/) — Rigorous theory
- [Stanford CS231n — CNNs for Visual Recognition](http://cs231n.stanford.edu/) — Computer Vision
- [Stanford CS224n — NLP with Deep Learning](http://web.stanford.edu/class/cs224n/) — NLP
- [Andrej Karpathy — Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) — Build from scratch

### Books
- *Hands-On Machine Learning* by Aurélien Géron — The best applied ML book
- *Deep Learning with Python* by François Chollet — Keras creator's guide
- *Designing Machine Learning Systems* by Chip Huyen — MLOps and production ML
- *Speech and Language Processing* by Jurafsky & Martin — NLP bible (free online)

### YouTube Channels
- **3Blue1Brown** — Visual math intuition (linear algebra, neural networks)
- **StatQuest** — Statistics and ML concepts explained simply
- **Yannic Kilcher** — ML paper explanations
- **Andrej Karpathy** — Building neural networks from scratch
- **sentdex** — Python ML tutorials

### Practice & Competitions
- [Kaggle](https://www.kaggle.com/) — Datasets, competitions, notebooks
- [Papers With Code](https://paperswithcode.com/) — Find implementations of research papers
- [HuggingFace](https://huggingface.co/) — Models, datasets, spaces
- [LeetCode (ML section)](https://leetcode.com/) — ML-flavored coding problems

---

## 🏗️ Projects Overview

| # | Project | Difficulty | Topics Covered |
|---|---------|------------|----------------|
| 1 | [House Price Predictor](07_Projects/project_1_house_price_predictor/) | ⭐⭐ Intermediate | pandas, sklearn, regression, pipelines |
| 2 | [Sentiment Analyzer](07_Projects/project_2_sentiment_analyzer/) | ⭐⭐⭐ Intermediate+ | NLP, transformers, HuggingFace, FastAPI |
| 3 | [Image Classifier](07_Projects/project_3_image_classifier/) | ⭐⭐⭐ Intermediate+ | PyTorch, CNNs, transfer learning |
| 4 | [RAG Chatbot](07_Projects/project_4_llm_chatbot/) | ⭐⭐⭐⭐ Advanced | embeddings, vector search, LLM APIs |
| 5 | [ML API Deployment](07_Projects/project_5_ml_api/) | ⭐⭐⭐ Intermediate+ | FastAPI, Docker, model serving |

---

*Happy learning! Remember: consistency > intensity. Show up every day, even if it's just 30 minutes.* 🚀
