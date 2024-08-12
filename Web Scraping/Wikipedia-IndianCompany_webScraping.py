from bs4 import BeautifulSoup
from requests import get
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_India'
page = get(url)

soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find('table', class_='wikitable sortable')
tableHeader = table.find_all('th')
Titles = [title.text.strip() for title in tableHeader]

row = []
for rows in table.find_all('tr')[1:]:
    cells = rows.find_all('td')
    row_data = [cell.text.strip() for cell in cells]
    row.append(row_data)

df = pd.DataFrame(row, columns=Titles)

df.to_csv(r'S:\VS code\python\Data _Analytics\Data_Analysis_Bootcamp\Web Scraping\2023LargestCompanyInIndia.csv', index=False)
