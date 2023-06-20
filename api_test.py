import requests

base_url = 'https://api.mendeley.com'
documents_endpoint = '/documents'

access_token = '83eGkxeG3I5COtC9'
headers = {
    'Authorization': 'Bearer ' + access_token,
    'Content-Type': 'application/json'
}

# Example GET request to retrieve documents
response = requests.get(base_url + documents_endpoint, headers=headers)

# Print the response
print(response.json())
