import requests

url = "https://api.github.com/events"
response = requests.get(url)
print(response.text)

# The requests library simplifies making HTTP requests. This is essential for interacting with web APIs (Application Programming Interfaces).