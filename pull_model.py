import requests
import json

# Load configuration from config.json
with open('config.json') as config_file:
    config = json.load(config_file)

API_KEY = config['api_key']
API_PULL_ENDPOINT = "http://localhost:11434/api/pull"

# Define the request data
data = {
    "model": "llama2"
}

# Define the headers
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# Make the request to pull the model
response = requests.post(API_PULL_ENDPOINT, headers=headers, data=json.dumps(data))

# Check the response status
if response.status_code == 200:
    print("Model pulled successfully")
else:
    print("Error pulling model:", response.status_code, response.text)