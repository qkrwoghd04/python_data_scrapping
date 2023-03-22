import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=100&sid2=264'

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')

dt_list = soup.select('ul.type06_headline > li > dl > dt > a')
newpapaers = soup.select('ul.type06_headline > li > dl > dd > span.writing')


# print(len(newpapaers))
# data = []
# for i in range(len(newpapaers)):
#     title = titles[i].text.strip()
#     newpaper = newpapaers[i].text.strip()
#     print(title)
    # data.append([title, newpapaers_name])

# df = pd.DataFrame(data, columns=['title', 'newpapaer'])
# df.to_excel('navernews.xlsx', index=False)
   
