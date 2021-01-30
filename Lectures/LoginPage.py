from tkinter import *


def register_user(): #register버튼을 눌렀을때, 텍스트 파일에 저장 하는 함수.

    username_info = username.get() # username의 값을 가져와 겟해!
    password_info = password.get()
    
    ##파일 열고 유저를 허락 하기 전에 우리는 유저가 합당한지를 체크해야한다.
    #기준 1. 패스워드는 8자리 이상인지?
    if len(password_info) >= 8:

        file = open(username_info+".txt", "w") #[username_info].txt - > youngho.txt, file의 권한 = w -> Write
        file.write("username: " + username_info)
        file.write("\n") #new line
        file.write("password: " + password_info)
        file.close()

        username_entry.delete(0,END)
        password_entry.delete(0,END)

        Label(screen1, text = "Registration Successful", fg = "green", font = ("Calibri", 13)).pack()
    else:
        password_entry.delete(0,END)
        Label(screen1, text = "The password has to be more than 8 digits!", fg = "red", font = ("Calibri", 13)).pack()

def register(): #회원가입
    global screen1
    screen1 = Toplevel(screen) # screen으로 인한 새로운 페이지
    screen1.title("Register")
    screen1.geometry("300x250")
    global username
    global password
    global username_entry
    global password_entry

    username = StringVar() 
    password = StringVar()

    Label(screen1, text = "Please enter your info below").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "User Name").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def login():
    pass

def login_page():
    global screen #전역 변수가 됨.
    screen = Tk() #현재 지역 변수 -> local variable -> 여기 함수 안에서만 쓸 수 있다.
    screen.geometry("300x350")
    screen.title("Manhattan Project Login Page")
    Label(text = "Manhattan Project Login Page", bg = "grey", width = 300, height = 2, font = ("calibri", 13)).pack()
    Label(text = "").pack() # 띄어쓰기
    Button(text = "Go to Login Page", width = 30, height = 2, command = login).pack()
    Label(text = "").pack() # 띄어쓰기
    Button(text = "Go to Register Page", width = 30, height = 2, command = register).pack()

    screen.mainloop()

login_page()