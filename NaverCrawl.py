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

#for loop전에 프린트보여주기
print(img)
print(img[0])
n = 1  # 이걸 안하면 덮어쓰기가 되어버림.
for i in img:
    #print(i['data-source'])
    imgUrl = i['data-source']
    with urlopen(imgUrl) as f:
        with open('./img_for_learning/' + plusUrl + str(n) + '.jpg', 'wb') as h:#그냥 w가아니라 wb인 이유는 이미지는 바이너리 파일이기 때문
            img = f.read()
            h.write(img)
    print("다운 완료:", n, "번째",imgUrl)
    n += 1

print('Download finish')
