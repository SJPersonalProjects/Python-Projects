# API Data Fetcher.

import requests

# Public API URL.
URL = "https://jsonplaceholder.typicode.com/users"

# Fetch data from the API.
response = requests.get(URL)

# Convert the JSON response to Python objects.
users = response.json()

# Display user information.
print("Users")
print("-" * 40)

for user in users:
    print(f"Name    :   {user['name']}")
    print(f"Email   :   {user['email']}")
    print(f"City    :   {user['address']['city']}")
    print("-" * 40)