This Repository contains `users.csv` and `repositories.csv`

`users.csv` : It has the following information about each user in Bangalore with over 100 followers, with fields:
- `login`: Their Github user ID
- `name`: Their full name
- `company`: The company they work at. Clean up company names.
- `location`: The city they are in
- `email`: Their email address
- `hireable`: Whether they are open to being hired
- `bio`: A short bio about them
- `public_repos`: The number of public repositories they have
- `followers`: The number of followers they have
- `following`: The number of people they are following
- `created_at`: When they joined Github

`repositories.csv` : It has these users' public repositories. For each user in users.csv, fetch up to the 500 most recently pushed repositories, with fields:
- `login`: The Github user ID (login) of the owner
- `full_name` : Full name of the repository
- `created_at`: When the repository was created
- `stargazers_count` : Number of stars the repository has
- `watchers_count` : Number of watchers the repository has
- `language` : The programming language the repository is written in
- `has_projects` : Whether the repository has projects enabled
- `has_wiki` : Whether the repository has a wiki
- `license_name` : Name of the license the repository is under

I use Python language and [GitHub REST API](https://docs.github.com/en/rest) to find all the necessary data for these two CSV files.
To be specific I use json and requests and pandas libraries

## Requests
To install `requests` library use the given following command in command prompt:

 ```sh
    pip install requests
```
## Pandas
To install `pandas` library use the given following command in command prompt:

```sh
    pip install pandas
```

The most preffered languages used by our sample of github users are:
1. JavaScript
2. HTML
3. CSS
4. Java
5. Kotlin
6. Jupyter Notebook
7. Python
8. TypeScript
9. Go
10. Shell

I would reccomend the use of Postman software for api testing and output.