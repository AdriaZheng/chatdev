import requests
import json

# Load configuration from config.json
with open('config.json') as config_file:
    config = json.load(config_file)

API_KEY = config['api_key']
API_ENDPOINT = config['api_endpoint']

# Define the request data
data = {
    "model": "llama2",
    "prompt": "Is the API key working?",
    "stream": False
}

# Define the headers
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# Make the request to test the API key
response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

# Check the response status
if response.status_code == 200:
    print("API key is working. Response:")
    print(response.json())
else:
    print("Error:", response.status_code, response.text)