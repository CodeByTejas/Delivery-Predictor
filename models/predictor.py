import pandas as pd
import numpy as np
from xgboost import XGBRegressor
import pickle
import os

class DeliveryPredictor:
    def __init__(self):
        self.model = XGBRegressor(
            n_estimators=100,
            learning_rate=0.1,
            max_depth=5,
            random_state=42
        )
        
        # Load pre-trained model if exists
        model_path = 'models/xgb_model.pkl'
        if os.path.exists(model_path):
            with open(model_path, 'rb') as f:
                self.model = pickle.load(f)
        
    def predict_demand(self, features):
        """Predict delivery demand based on input features"""
        feature_array = np.array([[
            features['temperature'],
            features['is_weekend'],
            features['is_holiday'],
            features['promotion_active'],
            features['hour'],
            features['day_of_week'],
            features['month'],
            features['is_lunch_time'],
            features['is_dinner_time']
        ]])
        
        prediction = self.model.predict(feature_array)[0]
        return round(prediction)