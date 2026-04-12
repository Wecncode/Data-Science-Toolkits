"""The complete lab. Demonstrates a production-grade Scikit-Learn pipeline predicting customer churn. It highlights how to handle real-world messy data before feeding it into the model."""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def build_churn_prediction_pipeline(filepath_or_url):
    """Builds a full Scikit-Learn pipeline for predicting customer churn."""
    
    print("1. Loading Data...")
    df = pd.read_csv(filepath_or_url)
    
    # --- REAL WORLD DATA CLEANING ---
    # In the Telco dataset, 'TotalCharges' looks like a number but is saved as a string.
    # Blank spaces " " represent new customers who haven't been charged yet.
    # We must force this to numeric, turning blanks into NaNs (which our pipeline will impute).
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    
    # Define features and target
    target = 'Churn'
    
    # We map the target 'Yes'/'No' to 1/0 for the algorithm
    y = df[target].map({'Yes': 1, 'No': 0})
    
    # Select a subset of highly relevant business features
    num_features = ['tenure', 'MonthlyCharges', 'TotalCharges']
    cat_features = ['Contract', 'InternetService', 'PaymentMethod', 'PaperlessBilling']
    
    X = df[num_features + cat_features]
    
    print("2. Splitting Data...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    print("3. Assembling Pipeline...")
    # Preprocessing for Numeric Data: Fill missing values with the median, then scale
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])
    
    # Preprocessing for Categorical Data: Fill missing values, then One-Hot Encode
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])
    
    # Combine into a ColumnTransformer
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, num_features),
            ('cat', categorical_transformer, cat_features)
        ])
    
    # Append a Gradient Boosting Classifier (often performs better than Random Forests on tabular data)
    full_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42))
    ])
    
    print("4. Training Pipeline (Transforms and Fits)...")
    full_pipeline.fit(X_train, y_train)
    
    print("5. Evaluating Model on Unseen Test Data...")
    predictions = full_pipeline.predict(X_test)
    
    print("\n" + "="*30)
    print("--- MODEL EVALUATION ---")
    print("="*30)
    print(f"Accuracy: {accuracy_score(y_test, predictions):.3f}\n")
    
    # In Churn, we care deeply about RECALL (finding all the people who actually churned)
    print("Classification Report:")
    print(classification_report(y_test, predictions, target_names=['Stayed (0)', 'Churned (1)']))
    
    print("Confusion Matrix:")
    cm = confusion_matrix(y_test, predictions)
    print(f"True Negatives (Correctly predicted stayed): {cm[0][0]}")
    print(f"False Positives (Falsely predicted churned): {cm[0][1]}")
    print(f"False Negatives (Missed churners - BAD!):    {cm[1][0]}")
    print(f"True Positives (Correctly predicted churn):  {cm[1][1]}")
    
    return full_pipeline

if __name__ == "__main__":
    # Using the standard IBM Telco Customer Churn dataset
    telco_url = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"
    model = build_churn_prediction_pipeline(telco_url)
