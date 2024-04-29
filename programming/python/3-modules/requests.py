import requests

# Make a GET request to a URL
response = requests.get('https://api.example.com/data')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print(response.text)
else:
    print(f'Error: {response.status_code}')

# query parameters
response = requests.get('https://api.example.com/data', params={'key1': 'value1', 'key2': 'value2'})

# post
response = requests.post('https://api.example.com/endpoint', json={'key': 'value'})

# Define custom headers
headers = {'User-Agent': 'Mozilla/5.0'}

# Make a GET request with custom headers
response = requests.get('https://api.example.com/data', headers=headers)

# handling exceptions
try:
    response = requests.get('https://api.example.com/data')
    response.raise_for_status()

except requests.exceptions.RequestException as e:
    print(f'Error: {e}')

