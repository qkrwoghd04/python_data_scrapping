import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
url = 'https://www.billboard.com/charts/hot-100/'

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')

titles = soup.select('li.o-chart-results-list__item > h3.c-title')
artist = soup.select('li.o-chart-results-list__item > span.c-label.a-no-trucate')

data = []
for i in range(len(titles)):
    title = titles[i].text.strip()
    artist_name = artist[i].text.strip()
    data.append([title, artist_name])

df = pd.DataFrame(data, columns=['Song name', 'Singer'])
df.to_excel('billboard_chart.xlsx', index=False)
   
