import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

class OutlierCapper(BaseEstimator, TransformerMixin):
    """
    A custom Scikit-Learn transformer that caps outliers in numeric columns 
    using the Interquartile Range (IQR) method. This prevents extreme values 
    (like a billionaire in a salary dataset) from skewing the model.
    """
    def __init__(self, factor=1.5):
        # The multiplier for the IQR. 1.5 is standard.
        self.factor = factor
        self.lower_bounds_ = {}
        self.upper_bounds_ = {}

    def fit(self, X, y=None):
        """Calculates and stores the bounds based on the training data."""
        # Ensure we are working with a Pandas DataFrame
        if not isinstance(X, pd.DataFrame):
            X = pd.DataFrame(X)
            
        for column in X.select_dtypes(include=[np.number]).columns:
            Q1 = X[column].quantile(0.25)
            Q3 = X[column].quantile(0.75)
            IQR = Q3 - Q1
            
            self.lower_bounds_[column] = Q1 - (self.factor * IQR)
            self.upper_bounds_[column] = Q3 + (self.factor * IQR)
            
        return self # fit() must always return self

    def transform(self, X, y=None):
        """Applies the capping to the data (training or testing sets)."""
        # We copy the data so we don't accidentally mutate the original
        X_capped = X.copy()
        if not isinstance(X_capped, pd.DataFrame):
            X_capped = pd.DataFrame(X_capped)
            
        for column, lower in self.lower_bounds_.items():
            upper = self.upper_bounds_[column]
            # Clip values to lie between the lower and upper bounds
            X_capped[column] = np.clip(X_capped[column], lower, upper)
            
        return X_capped

if __name__ == "__main__":
    # Create some dummy business data with massive outliers
    data = pd.DataFrame({
        'Customer_Age': [25, 30, 35, 40, 200, 22, 28, 900], # 200 and 900 are obvious errors
        'Monthly_Spend': [50, 60, 55, 70, 5000, 45, 65, 80]
    })
    labels = [0, 1, 0, 1, 1, 0, 1, 0]

    print("--- Original Data (Notice the extreme outliers) ---")
    print(data)

    # We can now plug our custom logic directly into a standard ML pipeline
    production_pipeline = Pipeline([
        ('outlier_handler', OutlierCapper(factor=1.5)),
        ('classifier', RandomForestClassifier(random_state=42))
    ])

    # The pipeline automatically calls .fit() then .transform() on our custom class
    production_pipeline.fit(data, labels)
    
    # Let's intercept the transformed data to prove our class worked
    cleaned_data = production_pipeline.named_steps['outlier_handler'].transform(data)
    
    print("\n--- Data after passing through Custom Transformer ---")
    print(cleaned_data)
