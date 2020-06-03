from tkinter import *
from selenium import webdriver
import bs4

window = Tk()
window.title("Web Opener")
#window.resizable(False, False)
window.configure(background='white')
window.geometry("210x230") 

def writeID():
    val = Entry.get(id_display)
    id_display.delete(0, END)
    return val

def writePwd():
    val = Entry.get(pwd_display)
    pwd_display.delete(0, END)
    return val

def openWeb():
    userID = str(writeID()) #get user ID from the fuction
    pwd = str(writePwd())

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors') #this will ignore certificate errors when opening web site

    driver = webdriver.Chrome(r"C:\Users\김영호\Desktop\github\chromedriver.exe") #must change to user's own path

    driver.implicitly_wait(3) #wait for 3 sec to wait for the chrome to be opend

    #facebook works
    driver.get("https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110")

    driver.find_element_by_name('email').send_keys(userID)
    driver.find_element_by_name('pass').send_keys(pwd) 
    #But this will lead to the "I'm not robot" page.
    driver.find_element_by_id('loginbutton').click()



id_display = Entry(window, width=28, justify="left") # justify = left로 하면 왼쪽부터 글 작성
pwd_display = Entry(window, width=28, justify="left")

id_display.grid(row = 0, column = 0, columnspan=4, pady=10, padx=4)
pwd_display.grid(row = 1, column = 0, columnspan=4, pady=10, padx=4)

open_web = Button(window, text = '아이디, 비번 입력 후 눌러주세요', width = 30, command = lambda: openWeb())

open_web.grid(row=3, column=3)


open_web.place(relx=0.5, rely=0.5, anchor=CENTER)


window.mainloop() #계속해서 loop이란걸 돌리면서 프로그램을 돌리는 코드
