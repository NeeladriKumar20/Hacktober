
import requests

# Set the API endpoint

url = "https://www.metaweather.com"

# Use the library to perform an HTTP GET request to the URL

response = requests.get(url)

# Print out the data

print(response.text)
