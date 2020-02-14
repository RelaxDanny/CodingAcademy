from tkinter import *
from selenium import webdriver
import bs4

window = Tk()
window.title("Web Opener")
window.resizable(False, False)
window.configure(background='white')
window.geometry("210x230") 

def writeID():
    val = Entry.get(id_display)
    display.delete(0, END)
    return id

def writePwd():
    val = Entry.get(pwd_display)
    display.delete(0, END)
    return pwd

def id_and_pwd():
    writeID()
    writePwd()
    

def openWeb():
    userID = str(writeID()) #get user ID from the fuction
    pwd = str(writePwd())

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors') #this will ignore certificate errors when opening web site

    driver = webdriver.Chrome(r"C:\Users\김영호\Desktop\github\chromedriver.exe") #must change to user's own path

    driver.implicitly_wait(3) #wait for 3 sec to wait for the chrome to be opend

    # driver.get("https://nid.naver.com/nidlogin.login")

    # driver.find_element_by_name('id').send_keys('')
    # driver.find_element_by_name('pw').send_keys('') 
    # #But this will lead to the "I'm not robot" page.
    # driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

    #facebook works
    driver.get("https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110")

    driver.find_element_by_name('email').send_keys(userID)
    driver.find_element_by_name('pass').send_keys(pwd) 
    #But this will lead to the "I'm not robot" page.
    driver.find_element_by_id('loginbutton').click()


id_display = Entry(window, width=28, justify="right") # justify = left로 하면 왼쪽부터 글 작성
pwd_display = Entry(window, width=28, justify="right")
display.grid(row = 0, column = 0, columnspan=4, pady=10, padx=4)

open_web = Button(window, text = '홈페이지 열기', width = 15, command = lambda: openWeb())
login_btn = Butto(window, text = '아이디, 비밀번호 설정', width = 15, command = id_and_pwd())

open_web.grid = (row = 3, column = 3)


def isEqualTo():
    val = Entry.get(display)
    result = eval(val)
    display.delete(0, END) #기존에 작성된 수식을 지우고
    display.insert(0, result) #결과값을 insert

def clear(where):
    display.delete(0, END) #C를 누르면 다 지우기


def btnPress(val):
    """
    val이라는 변수(1,2,3,+ ...)을 end에 insert하라는 말. 여기서 end는 맨뒤를 말함.
    """
    display.insert("end", val)

def myFunction():
    equation = Entry.get(display)
    myFun = float(equation) * 0.967 #1 = 0.33 = 3.3%의 세금
    display.delete(0, END)
    display.insert(0,myFun)


#FIRST ROW
#버튼 생성
b_my = Button(window, text='M', width=5, command = myFunction)
b_c = Button(window, text='C', width=5, command = lambda:clear(END)) #clear button
b_ce = Button(window, text = 'CE', width=5)
b_e = Button(window, text='=', width=5, command = isEqualTo) #parameter (매개변수)가 필요없으니 command만 사용



window.mainloop() #계속해서 loop이란걸 돌리면서 프로그램을 돌리는 코드
