import requests
import json
import matplotlib.pyplot as mpl


# Fetching data from the OpenWeatherMap API for the cities of California, Austin, Florida, New York and Chicago
WEATHER_API = "http://api.openweathermap.org/data/2.5/group?id=5332921,4671654,4155751,5128638,4887398&units=metric&appid=dccf59619c7116ade4620565792e69ea"

# API call to receive data
req = requests.get(WEATHER_API)
# Convert the response in JSON format
response = req.json()

# Process the data and store it in a JSON file
with open("weather.json", "w") as json_file:
    json.dump(response, json_file, indent=4)

# List of cities with information about the city from the "list" field
cities = []
[cities.append(city) for city in response["list"]]

# Receive city names
city_names = []
[city_names.append(city["name"]) for city in cities]

# Basic meteorological data for each city
indications = []
[indications.append(city["main"]) for city in cities]

min_temp, max_temp = [], []

# Receive temperature indications
for indication in indications:
    min_temp.append(indication["temp_min"])
    max_temp.append(indication["temp_max"])

# Create a new shape for the graph with dimensions 10x5
mpl.figure(figsize=(10, 5))
# City indices to display on X-axis
x = range(len(city_names))

# Create a bar graph for the minimum and maximum temperatures
mpl.bar(x, min_temp, width=0.3, label="Min temperature", align="center", color="lightgreen")
mpl.bar(x, max_temp, width=0.3, label="Max temperature", align="edge", color="orange")

mpl.title("Minimum and maximum temperature")
mpl.xlabel("City")
mpl.ylabel("Temperature °C")
mpl.xticks(x, city_names, rotation=0)
mpl.legend()
mpl.tight_layout()

mpl.savefig("weather_visualization.png")
mpl.show()