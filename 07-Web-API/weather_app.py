import random

def get_weather_prediction(city):
    """
    This function simulates a weather API. 
    In a real project, we would connect to an actual 
    service like Azure Maps or OpenWeather.
    """
    # Simulated data (Temperature in Celsius and Condition)
    temp = random.randint(-5, 40)
    conditions = ["Sunny", "Rainy", "Cloudy", "Snowing"]
    condition = random.choice(conditions)

    print(f"--- Weather Forecast for {city} ---")
    print(f"Current Temperature: {temp}°C")
    print(f"Condition: {condition}")

    # Logic-based Prediction (Decision Making)
    if temp > 30:
        return "It's going to be a hot day. Stay hydrated and wear light clothes!"
    elif 15 <= temp <= 30 and condition == "Sunny":
        return "Perfect weather! Great for a walk outside."
    elif condition == "Rainy":
        return "It's going to rain. Don't forget your umbrella!"
    elif temp < 5:
        return "It's freezing! Wear a heavy jacket."
    else:
        return "Weather looks stable. Have a great day!"

# Main Program
user_city = input("Enter your city name: ")
suggestion = get_weather_prediction(user_city)
print(f"Suggestion: {suggestion}")
