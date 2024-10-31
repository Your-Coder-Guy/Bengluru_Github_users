import requests
import json

query = "location:Bengaluru+followers:>100"
url = f"https://api.github.com/search/users?q={query}&sort=followers&order=desc"

response = requests.get(url)
data = response.json()  # Parse the JSON response

formatted_json = json.dumps(data, indent=4)  # Convert the JSON object to a formatted string

# Save the formatted JSON string to a file
F = open("user_data.json", "w")
F.write(formatted_json)
F.close()