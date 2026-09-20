"""
House Price Predictor — End-to-End Classical ML Pipeline
========================================================

Predict house prices using structured features.
Dataset: California Housing (sklearn) or Ames Housing (Kaggle)

Usage:
    python main.py
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import os


# =============================================================================
# Step 1: Data Loading & Exploration
# =============================================================================

def load_data():
    """Load the California Housing dataset and return as a DataFrame.

    Returns:
        pd.DataFrame: Full dataset with features and 'target' (median house value).
    """
    pass


def explore_data(df):
    """Print basic statistics and info about the dataset.

    Args:
        df (pd.DataFrame): The housing dataset.

    Prints:
        - Shape, dtypes, describe(), null counts
    """
    pass


def plot_eda(df):
    """Create exploratory visualizations.

    Args:
        df (pd.DataFrame): The housing dataset.

    Creates:
        - Distribution of target variable
        - Correlation heatmap
        - Top feature scatter plots vs target
        - Box plots for outlier detection
    """
    pass


# =============================================================================
# Step 2: Feature Engineering
# =============================================================================

def engineer_features(df):
    """Create new features and preprocess existing ones.

    Args:
        df (pd.DataFrame): Raw dataset.

    Returns:
        pd.DataFrame: Dataset with engineered features.

    Ideas:
        - Rooms per household
        - Bedrooms per room ratio
        - Population per household
        - Log-transform skewed features
    """
    pass


def split_data(df, target_col="target", test_size=0.2, random_state=42):
    """Split data into train and test sets.

    Args:
        df (pd.DataFrame): Full dataset.
        target_col (str): Name of target column.
        test_size (float): Fraction for test set.
        random_state (int): Random seed.

    Returns:
        tuple: (X_train, X_test, y_train, y_test)
    """
    pass


# =============================================================================
# Step 3: Model Training
# =============================================================================

def get_models():
    """Return a dictionary of models to try.

    Returns:
        dict: {model_name: model_instance}

    Models:
        - Linear Regression
        - Ridge Regression
        - Lasso Regression
        - Random Forest
        - Gradient Boosting
    """
    pass


def evaluate_models(models, X_train, y_train, cv=5):
    """Evaluate each model using cross-validation.

    Args:
        models (dict): {name: model} pairs.
        X_train (np.ndarray): Training features.
        y_train (np.ndarray): Training targets.
        cv (int): Number of CV folds.

    Returns:
        pd.DataFrame: Results table with model name, mean score, std.
    """
    pass


# =============================================================================
# Step 4: Hyperparameter Tuning
# =============================================================================

def tune_model(model, param_grid, X_train, y_train, cv=5):
    """Tune a model using GridSearchCV.

    Args:
        model: sklearn estimator.
        param_grid (dict): Hyperparameter grid.
        X_train (np.ndarray): Training features.
        y_train (np.ndarray): Training targets.
        cv (int): Number of CV folds.

    Returns:
        GridSearchCV: Fitted grid search object.
    """
    pass


# =============================================================================
# Step 5: Final Evaluation
# =============================================================================

def evaluate_final_model(model, X_test, y_test):
    """Evaluate the final model on the test set.

    Args:
        model: Trained sklearn model.
        X_test (np.ndarray): Test features.
        y_test (np.ndarray): Test targets.

    Returns:
        dict: {"MAE": ..., "RMSE": ..., "R2": ...}

    Also plots:
        - Predicted vs actual scatter plot
        - Residual distribution
    """
    pass


# =============================================================================
# Step 6: Save & Load Model
# =============================================================================

def save_model(model, filepath="models/house_price_model.joblib"):
    """Save the trained model to disk.

    Args:
        model: Trained sklearn model or pipeline.
        filepath (str): Path to save the model.
    """
    pass


def load_model(filepath="models/house_price_model.joblib"):
    """Load a saved model from disk.

    Args:
        filepath (str): Path to the saved model.

    Returns:
        Loaded model.
    """
    pass


def predict(features, model_path="models/house_price_model.joblib"):
    """Make a prediction using the saved model.

    Args:
        features (dict or pd.DataFrame): Input features.
        model_path (str): Path to saved model.

    Returns:
        float: Predicted house price.
    """
    pass


# =============================================================================
# Main Pipeline
# =============================================================================

def main():
    """Run the full house price prediction pipeline.

    Steps:
        1. Load and explore data
        2. Engineer features
        3. Split into train/test
        4. Train and compare models
        5. Tune best model
        6. Evaluate on test set
        7. Save model
    """
    print("=" * 60)
    print("House Price Predictor — ML Pipeline")
    print("=" * 60)

    # Step 1: Load data
    print("\n📊 Step 1: Loading data...")
    # df = load_data()
    # explore_data(df)
    # plot_eda(df)

    # Step 2: Feature engineering
    print("\n🔧 Step 2: Engineering features...")
    # df = engineer_features(df)

    # Step 3: Split data
    print("\n✂️  Step 3: Splitting data...")
    # X_train, X_test, y_train, y_test = split_data(df)

    # Step 4: Train models
    print("\n🤖 Step 4: Training models...")
    # models = get_models()
    # results = evaluate_models(models, X_train, y_train)
    # print(results)

    # Step 5: Tune best model
    print("\n🎯 Step 5: Tuning best model...")
    # param_grid = {...}
    # grid_search = tune_model(best_model, param_grid, X_train, y_train)

    # Step 6: Final evaluation
    print("\n📈 Step 6: Final evaluation...")
    # metrics = evaluate_final_model(grid_search.best_estimator_, X_test, y_test)
    # print(metrics)

    # Step 7: Save model
    print("\n💾 Step 7: Saving model...")
    # save_model(grid_search.best_estimator_)

    print("\n✅ Pipeline complete!")


if __name__ == "__main__":
    main()
