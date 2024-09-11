import requests
from bs4 import BeautifulSoup

# 원하는 웹 페이지의 URL
url = "https://news.naver.com/"

# 웹 페이지 가져오기
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 특정 태그 안의 텍스트 추출하기 (예: 모든 p 태그의 내용)
for p in soup.find_all('p'):
    print(p.text)