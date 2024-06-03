import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import requests, csv
import pandas as pd
from bs4 import BeautifulSoup

# Download content from the webpage.
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_smartphone_penetration'
data = requests.get(url).text

# Cteate beautifulsoup object
soup = BeautifulSoup(data, 'html.parser')

# In the event there are multiple html tables within the same page, select the first one of the page.
tables = soup.find_all('table')
first_table = tables[0]

# Defining dataset format
df = pd.DataFrame(columns=['Rank', 'Country', 'Population', 'Smartphone users', 'Smartphone penetration'])

# Populating necessary data and perform a preliminary data sanitization.
for row in first_table.tbody.find_all('tr'):
    # Search all data in the first column
    columns = row.find_all('td')

    if(columns != []):
        rank = columns[0].text.strip()
        country = columns[1].text.strip()
        population = columns[2].text.strip()
        smartphone_users = columns[3].text.strip()
        smartphone_penetration = columns[4].text.strip()

        df = df.append({'Rank': rank,
                        'Country': country,
                        'Population': population,
                        'Smartphone_users': smartphone_users,
                        'Smartphone_penetration': smartphone_penetration},
                        ignore_index=True)

print(df.head())