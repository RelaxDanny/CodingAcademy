from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus #한번 검색하면 ASCII코드로 변환 된거 보여주기 그렇기 땜누에 사용
import ssl

context = ssl._create_unverified_context()

baseUrl = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
plusUrl = input("검색어를 입력하세요 : ")
result = urlopen(baseUrl, context= context)
url = baseUrl + quote_plus(plusUrl)

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser') #html에 저장된 url을 분석
img = soup.find_all(class_="_img")

print(img[0])
