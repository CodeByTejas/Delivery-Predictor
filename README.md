# Food Delivery Demand Forecasting

A machine learning system that predicts food delivery order volumes based on weather, time patterns, and other factors.

## Features

- Real-time weather data integration
- Time-based demand prediction
- Holiday and promotion impact analysis
- XGBoost-based prediction model
- Interactive command-line interface

## Project Structure

```
├── models/
│   └── predictor.py         # ML model implementation
├── utils/
│   ├── data_generator.py    # Training data generation
│   ├── time_features.py     # Time-based feature extraction
│   └── weather.py          # Weather API integration
├── predict_demand.py        # Main prediction script
├── train_model.py          # Model training script
└── requirements.txt        # Project dependencies
```

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
Create a `.env` file with your Weather API key:
```
WEATHER_API_KEY=your_api_key_here
```

## Usage

1. Train the model:
```bash
python train_model.py
```

2. Make predictions:
```bash
python predict_demand.py
```

Follow the interactive prompts to:
- Enter a city name
- Specify if it's a holiday
- Indicate if there's an active promotion

## Features Used in Prediction

- Weather conditions (temperature)
- Time of day (lunch/dinner hours)
- Day of week (weekday/weekend)
- Holidays
- Active promotions

## Model Details

The system uses XGBoost for predictions with the following features:
- Temperature
- Weekend/weekday status
- Holiday status
- Promotion status
- Hour of day
- Day of week
- Month
- Lunch/dinner time periods

## Requirements

- Python 3.8+
- Dependencies listed in requirements.txt
- Weather API key from weatherapi.com
