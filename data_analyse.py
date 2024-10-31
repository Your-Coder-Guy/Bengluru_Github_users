import json
import requests

# Load the JSON data from the file
with open("user_data.json") as f:
    data = json.load(f)

data = data["items"]
writing_data = []
base_url = "https://api.github.com/users/"

for user in data:
    login = user["login"]
    user_url = base_url + login
    response = requests.get(user_url)
    
    if response.status_code == 200:
        user_data = response.json()
        name = user_data.get("name")
        location = user_data.get("location")
        email = user_data.get("email")
        hireable = user_data.get("hireable")
        bio = user_data.get("bio")
        followers = user_data.get("followers")
        following = user_data.get("following")
        public_repos = user_data.get("public_repos")
        created_at = user_data.get("created_at")
        company = user_data.get("company")
        
        writing_data.append({
            "login": login,
            "name": name,
            "location": location,
            "email": email,
            "hireable": hireable,
            "bio": bio,
            "followers": followers,
            "following": following,
            "public_repos": public_repos,
            "created_at": created_at,
            "company": company
        })
    else:
        print(f"Failed to fetch data for user: {login}")

# Optionally, save the writing_data to a file
with open("detailed_user_data.json", "w") as f:
    json.dump(writing_data, f, indent=4)