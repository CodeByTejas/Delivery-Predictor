from datetime import datetime

def get_time_features(dt=None):
    """Extract time-based features from a datetime object"""
    if dt is None:
        dt = datetime.now()
        
    return {
        'hour': dt.hour,
        'day_of_week': dt.weekday(),
        'month': dt.month,
        'is_weekend': dt.weekday() >= 5,
        'is_lunch_time': 11 <= dt.hour <= 14,
        'is_dinner_time': 18 <= dt.hour <= 21
    }