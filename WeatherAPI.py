import requests

def get_weather(city_name):
    api_key = "377ca3419dc66814f7f954f0691349e9"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # Extract and display relevant weather information
        main = data['main']
        weather = data['weather'][0]
        
        temperature = main['temp']
        humidity = main['humidity']
        description = weather['description']
        
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.capitalize()}" + "\n")
    else:
        print("City not found or an error occurred.")

def main():
    city_name = input("\n" + "Enter the name of the city: ")
    get_weather(city_name)

if __name__ == "__main__":
    main()