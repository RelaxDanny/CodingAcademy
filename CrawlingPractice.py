# #if bs4 is not working, use selenium

# from bs4 import BeautifulSoup
# from urllib.request import urlopen

# #response = urlopen('https://en.wikipedia.org/wiki/Main_Page')

# with urlopen('https://en.wikipedia.org/wiki/Main_Page') as response:
#     soup = BeautifulSoup(response, 'html.parser')
#     for anchor in soup.select("span.ah_k"):
#         print(anchor)
from selenium import webdriver
import bs4
driver = webdriver.Chrome(r"C:\Users\김영호\Desktop\github\chromedriver.exe")
driver.implicitly_wait(3) #wait for 3 to wait for the chrome to be opend

# driver.get("https://nid.naver.com/nidlogin.login")

# driver.find_element_by_name('id').send_keys('dannyinsuny')
# driver.find_element_by_name('pw').send_keys('!Smlal153') 
# #But this will lead to the "I'm not robot" page.
# driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

driver.get('https://order.pay.naver.com/home')
html = driver.page_source
soup = bs4.BeautifulSoup(html, 'html.parser')
notices = soup.findall("a", {"class":"goods"})

for n in notices:
    print(n.text.strip())