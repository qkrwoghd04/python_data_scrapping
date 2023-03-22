import requests
from bs4 import BeautifulSoup
import pandas as pd

# 멜론 음원 차트 URL
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
url = 'https://www.melon.com/chart/index.htm'

# requests 모듈을 사용하여 웹 페이지에 접속
response = requests.get(url, headers=headers)
# # Beautiful Soup을 사용하여 HTML 코드 파싱

soup = BeautifulSoup(response.text, 'html.parser')

# 노래 제목과 가수명 가져오기
titles = soup.select('div.ellipsis.rank01 > span > a')
artists = soup.select('div.ellipsis.rank02 > span > a')

# 데이터를 저장할 리스트 생성
data = []
for i in range(len(titles)):
    title = titles[i].text
    artist = artists[i].text
    data.append([title, artist])

# 데이터프레임 생성
df = pd.DataFrame(data, columns=['노래 제목', '가수명'])

# 엑셀 파일로 저장
df.to_excel('melon_chart.xlsx', index=False)