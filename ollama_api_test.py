from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

def load_config(config_file_path='config.json'):
    with open(config_file_path) as config_file:
        return json.load(config_file)

config = load_config()
API_KEY = config['api_key']
API_ENDPOINT = config['api_endpoint']

@app.route('/')
def index():
    return "Welcome to the Ollama API!"

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt', '')
    model = data.get('model', 'llama2')

    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    request_data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(request_data))

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": response.text}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)