from tkinter import *
window = Tk()
window.title("Calculator")
window.resizable(False, False) #가로 세로 크기조정 막는 코드
window.configure(background='grey') #색은 승현이가 원하는 색으로 
window.geometry("210x230") #가로 x 세로 크기

display = Entry(window, width=28, justify="right") # justify = left로 하면 왼쪽부터 글 작성

#FIRST ROW
#버튼 생성
b_my = Button(window, text='M', width=5)
b_c = Button(window, text='C', width=5)
b_ce = Button(window, text = 'CE', width=5)
b_e = Button(window, text='=', width=5)

#lambda라는것을 사용하면 연속으로 호출 가능
#그냥 command = btnPress()를 사용하게 되면 매개변수를 사용 못함 -> (val) 그래서 람다 사용
#이미 입력된 상태로 디스플레이가 나옴
#SECOND ROW
b_2 = Button(window, text = '2', width=5)
b_1 = Button(window, text = '1', width=5) 
b_3 = Button(window, text = '3', width=5)
b_a = Button(window, text = '+', width=5)

#THIRD ROW
b_4 = Button(window, text = '4', width=5)
b_5 = Button(window, text = '5', width=5)
b_6 = Button(window, text = '6', width=5)
b_s = Button(window, text = '-', width=5)

#FOURTH ROW
b_7 = Button(window, text = '7', width=5)
b_8 = Button(window, text = '8', width=5)
b_9 = Button(window, text = '9', width=5)
b_m = Button(window, text = '*', width=5)

#FIFTH ROW
b_0 = Button(window, text = '0', width=5)
b_v = Button(window, text = '+/-', width=5)
b_p = Button(window, text = '.', width=5)
b_d = Button(window, text = '/', width=5)


display.grid(row = 0, column = 0, columnspan=4, pady=10, padx=4)
#버튼의 grid설정 (폭, 넓이)
b_my.grid(row=1, column=0, pady=3)
b_c.grid(row=1,  column=1)
b_ce.grid(row=1, column=2)
b_e.grid(row=1,  column=3)

b_1.grid(row=2, column=0, pady=3)
b_2.grid(row=2, column=1)
b_3.grid(row=2, column=2)
b_a.grid(row=2, column=3)

b_4.grid(row=3, column=0, pady=3)
b_5.grid(row=3, column=1)
b_6.grid(row=3, column=2)
b_s.grid(row=3, column=3)


b_7.grid(row=4, column=0, pady=3)
b_8.grid(row=4, column=1)
b_9.grid(row=4, column=2)
b_m.grid(row=4, column=3)

b_0.grid(row=5, column=0, pady=3)
b_v.grid(row=5, column=1)
b_p.grid(row=5, column=2)
b_d.grid(row=5, column=3)


window.mainloop() #계속해서 loop이란걸 돌리면서 프로그램을 돌리는 코드
