# 🏠 Project 1: House Price Predictor

**End-to-End Classical Machine Learning**

| | |
|---|---|
| **Difficulty** | ⭐⭐ Intermediate |
| **Time Estimate** | 8–12 hours |
| **Prerequisites** | NumPy, Pandas, Visualization, Classical ML |

---

## Overview

Build a complete machine learning pipeline to predict house prices from structured features. This is the quintessential regression project — you'll go from raw data to a saved model, touching every stage of the ML workflow.

**Goal:** Predict house sale prices given features like square footage, number of bedrooms, location, etc.

---

## Dataset

Choose one:
- **California Housing** (built into sklearn) — `sklearn.datasets.fetch_california_housing()`
- **Ames Housing** — [Kaggle link](https://www.kaggle.com/c/house-prices-advanced-regression-techniques) (richer features, more preprocessing needed)

The California Housing dataset is great for getting started quickly. The Ames dataset is better for practicing feature engineering.

---

## Steps

### Step 1: Data Exploration & Visualization
- Load the dataset and inspect shape, dtypes, basic stats
- Check for missing values, duplicates, outliers
- Plot distributions of target variable (price)
- Create correlation heatmap
- Scatter plots of top features vs. price

### Step 2: Feature Engineering
- Handle missing values (imputation strategies)
- Create new features (e.g., total rooms, price per sqft ratios)
- Encode categorical variables (one-hot, ordinal)
- Scale numerical features (StandardScaler, MinMaxScaler)
- Feature selection — drop low-correlation or redundant features

### Step 3: Model Selection
Try multiple models and compare:
- **Linear Regression** — simple baseline
- **Ridge / Lasso** — regularized linear models
- **Random Forest** — ensemble of decision trees
- **Gradient Boosting** (XGBoost or sklearn) — state-of-the-art for tabular data

### Step 4: Hyperparameter Tuning
- Use `GridSearchCV` or `RandomizedSearchCV`
- Tune the top 2 models from Step 3
- Use 5-fold cross-validation
- Track results in a comparison table

### Step 5: Final Evaluation
- Train best model on full training set
- Evaluate on held-out test set
- Metrics: MAE, RMSE, R² Score
- Plot predicted vs. actual prices
- Analyze residuals — where does the model fail?

### Step 6: Save the Model
- Save the trained model with `joblib`
- Save the preprocessing pipeline too
- Write a simple `predict()` function that loads and uses the model

---

## What You'll Learn

| Skill | Notebook Topic |
|-------|---------------|
| Data loading & cleaning | `03_Pandas/` |
| Exploratory data analysis | `04_Visualization/` |
| Feature engineering | `06_Classical_ML/` |
| Model training & evaluation | `06_Classical_ML/` |
| Cross-validation & tuning | `06_Classical_ML/` |
| sklearn Pipelines | `06_Classical_ML/` |
| Model serialization | `12_MLOps/` |

---

## Deliverables Checklist

- [ ] Jupyter notebook with full EDA (at least 5 visualizations)
- [ ] Feature engineering pipeline (reproducible)
- [ ] At least 3 models compared with cross-validation scores
- [ ] Hyperparameter tuning results table
- [ ] Final model evaluation on test set (MAE, RMSE, R²)
- [ ] Predicted vs. actual scatter plot
- [ ] Saved model file (`.joblib`)
- [ ] Clean `main.py` with modular functions
- [ ] Brief write-up: what worked, what didn't, what you'd try next

---

## Starter Code

See [`main.py`](main.py) for the project skeleton.

```
project_1_house_price_predictor/
├── README.md
├── main.py              # Main pipeline script
├── notebook.ipynb       # EDA and experimentation (create this)
├── models/              # Saved models go here (create this)
└── data/                # Downloaded data (create this)
```
