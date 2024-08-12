from bs4 import BeautifulSoup
from requests import get
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_galaxies'
page = get(url)

soup = BeautifulSoup(page.text, 'html.parser')

def createDataFrame(index):
    table = soup.find_all('table')[index]
    tableHeader = table.find_all('th')

    Titles = [ header.text.strip() for header in tableHeader]

    rows = []

    for row in table.find_all('tr')[1:]:
        cells = row.find_all('td')
        row_data = [cell.text.strip() for cell in cells]
        rows.append(row_data)
    
    return pd.DataFrame(rows, columns=Titles)

df_nakedEyeGalaxies = createDataFrame(1)
df_GalaxiesByBrightnessPower = createDataFrame(10)
df_MostRemoteGalaxyPerYear = createDataFrame(9)

def save_to_single_csv(file_name, data_frames, titles):
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        for df, title in zip(data_frames, titles):
            file.write(f'\n{title}\n')
            df.to_csv(file, index=False, header=True, mode='a')
            file.write('\n')

data_frames = [df_nakedEyeGalaxies, df_GalaxiesByBrightnessPower, df_MostRemoteGalaxyPerYear]
titles = ['Naked Eye Galaxies', 'Galaxies by Brightness and Power', 'Most Remote Galaxy Record-holders']

save_to_single_csv('Galaxies.csv', data_frames, titles)
