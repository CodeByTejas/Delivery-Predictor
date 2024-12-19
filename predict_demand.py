from utils.weather import fetch_weather_data
from utils.time_features import get_time_features
from models.predictor import DeliveryPredictor

def get_user_inputs():
    """Get user inputs for prediction"""
    print("\n=== Food Delivery Demand Predictor ===\n")
    
    # Get location
    city = input("Enter city name (e.g., London): ")
    
    # Get weather data
    weather_data = fetch_weather_data(city)
    if not weather_data:
        print("Error fetching weather data. Using default values.")
        weather_data = {'temperature': 20, 'is_raining': False}
    
    # Get time features
    time_features = get_time_features()
    
    # Get additional inputs
    is_holiday = input("Is today a holiday? (y/n): ").lower() == 'y'
    promotion_active = input("Is there an active promotion? (y/n): ").lower() == 'y'
    
    # Combine all features
    features = {
        **weather_data,
        **time_features,
        'is_holiday': is_holiday,
        'promotion_active': promotion_active
    }
    
    return features

def main():
    while True:
        # Get user inputs
        features = get_user_inputs()
        
        # Make prediction
        predictor = DeliveryPredictor()
        predicted_orders = predictor.predict_demand(features)
        
        # Display results
        print("\n=== Prediction Results ===")
        print(f"Predicted number of orders: {predicted_orders}")
        print(f"Temperature: {features['temperature']}°C")
        print(f"Time period: {'Lunch time' if features['is_lunch_time'] else 'Dinner time' if features['is_dinner_time'] else 'Regular hours'}")
        print(f"Day type: {'Weekend' if features['is_weekend'] else 'Weekday'}")
        print(f"Promotion active: {'Yes' if features['promotion_active'] else 'No'}")
        
        # Ask if user wants to make another prediction
        if input("\nMake another prediction? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()