""" Lab Starter Code: Filling in the missing logic to clean a simulated messy dataset without loops."""

import pandas as pd
import numpy as np

def clean_sales_data(filepath):
    """
    Reads a messy CSV and cleans it using pure Pandas vectorization.
    NO FOR LOOPS ALLOWED.
    """
    # 1. Load the data
    df = pd.read_csv(filepath)
    
    # TODO: The 'Price' column has dollar signs and commas (e.g., "$1,200.50"). 
    # Strip the string characters and convert to a float.
    df['Price'] = ... 
    
    # TODO: The 'Date' column is a mix of formats. Convert to standard datetime.
    # Coerce errors to NaT (Not a Time).
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    
    # TODO: Drop any rows where the 'Date' or 'Price' is missing (NaN)
    df_cleaned = ...
    
    # TODO: Group by 'Category' and find the total sum of 'Price' for each
    category_totals = ...
    
    return category_totals

if __name__ == "__main__":
    # Students will run this against a provided 'messy_sales.csv'
    # result = clean_sales_data('messy_sales.csv')
    # print(result)
    pass
