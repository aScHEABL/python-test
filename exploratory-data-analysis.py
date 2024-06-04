import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import requests
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import seaborn as sns

# Download content from the webpage
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_smartphone_penetration'
data = requests.get(url).text

# Create BeautifulSoup object
soup = BeautifulSoup(data, 'html.parser')

# Select the first table on the page
tables = soup.find_all('table')
first_table = tables[0]

# Define dataset format
df = pd.DataFrame(columns=['Rank', 'Country', 'Population', 'Smartphone_users', 'Smartphone_penetration'])

# Populate necessary data and perform a preliminary data sanitization
for row in first_table.tbody.find_all('tr'):
    columns = row.find_all('td')
    if len(columns) >= 5:  # Ensure there are enough columns
        rank = columns[0].text.strip()
        country = columns[1].text.strip()
        population = columns[2].text.strip().replace(',', '').replace('M', 'e6').replace('B', 'e9')
        smartphone_users = columns[3].text.strip().replace(',', '').replace('M', 'e6').replace('B', 'e9')
        smartphone_penetration = columns[4].text.strip().replace('%', '')

        df = df.append({'Rank': rank,
                        'Country': country,
                        'Population': population,
                        'Smartphone_users': smartphone_users,
                        'Smartphone_penetration': smartphone_penetration},
                       ignore_index=True)

# Convert columns to numeric types
df['Rank'] = pd.to_numeric(df['Rank'], errors='coerce')
df['Population'] = pd.to_numeric(df['Population'].apply(pd.eval), errors='coerce')
df['Smartphone_users'] = pd.to_numeric(df['Smartphone_users'].apply(pd.eval), errors='coerce')
df['Smartphone_penetration'] = pd.to_numeric(df['Smartphone_penetration'], errors='coerce')

# Drop rows with missing values
df = df.dropna()

# Display the cleaned DataFrame
print(df.head())

# Summary statistics
print("Summary Statistics:")
print(df.describe())

# Set plot style
sns.set(style="whitegrid")

# Plot smartphone penetration distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Smartphone_penetration'], kde=True, bins=30)
plt.title('Distribution of Smartphone Penetration')
plt.xlabel('Smartphone Penetration (%)')
plt.ylabel('Frequency')
plt.savefig('smartphone_penetration_distribution.png')

# Scatter plot of population vs. smartphone users
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Population', y='Smartphone_users', data=df)
plt.title('Population vs. Smartphone Users')
plt.xlabel('Population')
plt.ylabel('Smartphone Users')
plt.savefig('population_vs_smartphone_users.png')

# Bar plot of top 10 countries by smartphone penetration
top_10_countries = df.nlargest(10, 'Smartphone_penetration')

plt.figure(figsize=(14, 8))
sns.barplot(x='Smartphone_penetration', y='Country', data=top_10_countries)
plt.title('Top 10 Countries by Smartphone Penetration')
plt.xlabel('Smartphone Penetration (%)')
plt.ylabel('Country')
plt.savefig('top_10_countries_smartphone_penetration.png')

# Save cleaned data to a CSV file
df.to_csv('cleaned_smartphone_penetration_data.csv', index=False)
