import pandas as pd
import matplotlib.pyplot as plt

repo = pd.read_csv('repositories.csv')

# Count the number of repositories per language

languages_counts = repo['language'].value_counts()
print(languages_counts)