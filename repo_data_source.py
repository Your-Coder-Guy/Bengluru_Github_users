import json
import requests
import pandas as pd

users_df = pd.read_csv('users.csv')
users = users_df.get('login')
del users_df
def url(username):
    return f"https://api.github.com/users/{username}/repos"

data = []
F = open('access_token.txt', 'r')
access_token = F.read()
F.close()

headers = {
    'Authorization': f'token {access_token}'
}

for user in users:
    response = requests.get(url(user), headers=headers)
    if response.status_code == 200:
        user_data_list = response.json()
        for repo in user_data_list:
            license = repo.get("license", {})
            if license is not None:
                license = license.get("key")
            data.append({
                "login": repo.get("owner", {}).get("login"),
                "full_name": repo.get("full_name"),
                "created_at": repo.get("created_at"),
                "stargazers_count": repo.get("stargazers_count"),
                "watchers_count": repo.get("watchers_count"),
                "language": repo.get("language"),
                "has_projects": repo.get("has_projects"),
                "has_wiki": repo.get("has_wiki"),
                "license": license,
                "pushed_at": repo.get("pushed_at")
            })
    else:
        print(f"Error: {response.status_code}")

# Sort the data list based on the "pushed_at" key in descending order
sorted_data = sorted(data, key=lambda x: x["pushed_at"], reverse=True)

sorted_data = sorted_data[0:500]

print(len(sorted_data))

# Save the data to a JSON file
with open('repos.json', 'w') as f:
    json.dump(sorted_data, f,indent=4)

