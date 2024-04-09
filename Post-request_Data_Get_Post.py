#Data_Get_Post.py file Post request 

import requests

# URL of the Flask API endpoint
url = 'http://localhost:5000/data'

# JSON data to be sent in the request body
data = {
    "id":4,  
    "name":"sid", 
    "city":"Ale", 
    "Edu":"BCom"
}

# Send a POST request to add the data
response = requests.post(url, json=data)

# Print the response from the API
print(response.json())
