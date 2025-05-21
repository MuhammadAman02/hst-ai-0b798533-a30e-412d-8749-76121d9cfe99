import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

class DataProcessor:
    def __init__(self):
        self.scaler = StandardScaler()
        self.processed_data = None

    def process_data(self, df):
        # Assuming the last column is the target variable
        X = df.iloc[:, :-1]
        y = df.iloc[:, -1]

        # Normalize numerical features
        X_scaled = self.scaler.fit_transform(X)

        # Convert back to DataFrame
        X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns)

        self.processed_data = (X_scaled_df, y)
        return X_scaled_df, y

    def get_processed_data(self):
        if self.processed_data is None:
            raise ValueError("Data has not been processed yet. Please process the data first.")
        return self.processed_data