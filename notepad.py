from tkinter import *

ui = Tk() #Tk라는 함수를 ui라는 이름으로 지속적으로 사용하기 위함
ui.title("Calculator")
ui.resizable(False, False)
ui.configure(background = 'grey')
ui.geometry("210x230")

display = Entry(ui, width = 28, justify='right')



ui.mainloop() #loop을 통해서 계속 실행