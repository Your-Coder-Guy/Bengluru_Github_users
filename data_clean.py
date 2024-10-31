import json

data = json.load(open("detailed_user_data.json"))
for user in data:
    bio = user["bio"]
    if bio is not None:
        bio = bio.split(" ")
        bio = [word for word in bio if word.startswith("@")]
        bio = " ".join(bio)
        company = user["company"]
        if company is not None and user["company"].lower() not in bio.lower():
            company += " " + bio
            company = company.replace("@", "")
            company = company.upper()
        user["company"] = company

dict_data = {"login":[], "name":[], "location":[], "email":[], "hireable":[], "bio":[], "followers":[], "following":[], "public_repos":[], "created_at":[], "company":[]}
for user in data:
    dict_data["login"].append(user["login"])
    dict_data["name"].append(user["name"])
    dict_data["location"].append(user["location"])
    dict_data["email"].append(user["email"])
    dict_data["hireable"].append(user["hireable"])
    dict_data["bio"].append(user["bio"])
    dict_data["followers"].append(user["followers"])
    dict_data["following"].append(user["following"])
    dict_data["public_repos"].append(user["public_repos"])
    dict_data["created_at"].append(user["created_at"])
    dict_data["company"].append(user["company"])

import pandas as pd
df = pd.DataFrame(dict_data)
df.to_csv("users.csv", index=False)
# The code reads the JSON data from the file detailed_user_data.json and extracts the bio and company information from the user data.

