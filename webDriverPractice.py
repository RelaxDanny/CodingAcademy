
from selenium import webdriver
import bs4
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(r"C:\Users\김영호\Desktop\github\chromedriver.exe")

driver.implicitly_wait(3) #wait for 3 to wait for the chrome to be opend

# driver.get("https://nid.naver.com/nidlogin.login")

# driver.find_element_by_name('id').send_keys('')
# driver.find_element_by_name('pw').send_keys('') 
# #But this will lead to the "I'm not robot" page.
# driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

#facebook works
driver.get("https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110")

driver.find_element_by_name('email').send_keys('')
driver.find_element_by_name('pass').send_keys('') 
#But this will lead to the "I'm not robot" page.
driver.find_element_by_id('loginbutton').click()


# driver.get('https://order.pay.naver.com/home')
# html = driver.page_source
# soup = bs4.BeautifulSoup(html, 'html.parser')
# notices = soup.findall("a", {"class":"goods"})

for n in notices:
    print(n.text.strip())