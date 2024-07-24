import requests
import json

# Load configuration from config.json
with open('config.json') as config_file:
    config_content = config_file.read()
    print("Config file content (raw):")
    print(repr(config_content))  # Use repr to show hidden characters
    config = json.loads(config_content)

API_KEY = config['api_key']
API_ENDPOINT = config['api_endpoint'].strip()

# Define the request data
data = {
    "model": "llama2",
    "prompt": "Why is the sky so blue?",
    "stream": False
}

# Define the headers
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# Make the request
response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

# Check the response status
if response.status_code == 200:
    response_text = response.text
    data = json.loads(response_text)
    actual_response = data.get("response")
    print(actual_response)
else:
    print("Error:", response.status_code, response.text)
