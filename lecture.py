from tkinter import * #Tkinter lib take all * = all

ui = Tk() # class  = book, we use ui variable to clarify 
ui.title("Calculator") # our ui's title = calculator
ui.resizable(False, False) # parameter = 2
ui.geometry("280x300")
ui.configure(background = 'green')
display = Entry(ui, width=28, justify='right')
display.grid(row = 0, column = 0 , columnspan = 4, pady=10, padx=4)

def myFunction():
    value = Entry.get(display) #get display's entry
    myFun = eval(value) * 29 / 30 # tax calc
    display.delete(0, END)
    display.insert(0, myFun)
def cancel():
    display.delete(0, 1)
def cancel_all():
    display.delete(0, END)
def equal():
    value = Entry.get(display)
    func = eval(value)
    display.delete(0, END)
    display.insert(0, func)
def zero():
    display.insert(END, 0)
def one():
    display.insert(END, 1)
def Two():
    display.insert(END, 2)
def Three():
    display.insert(END, 3)
def four():
    display.insert(END, 4)
def five():
    display.insert(END, 5)
def six():
    display.insert(END, 6)
def seven():
    display.insert(END, 7)
def eight():
    display.insert(END, 8)
def nine():
    display.insert(END, 9)
def plus():
    display.insert(END, '+')
def minus():
    display.insert(END, '-')
def mult():
    display.insert(END, '*')
def div():
    display.insert(END, '/')
def negative():
    display.insert(0, '-')


#Search - bar 

#button = btn
btn_my = Button(ui, text='M', width = 5, command = myFunction)
btn_c = Button(ui, text='C', width = 5, command = cancel)
btn_CE = Button(ui, text='CE', width = 5, command = cancel_all)
btn_e = Button(ui, text='=', width = 5, command = equal)
btn_zero = Button(ui, text='0', width = 5, command = zero)
btn_one = Button(ui, text='1', width = 5, command = one)
btn_Two = Button(ui, text='2', width = 5, command = Two)
btn_Three = Button(ui, text='3', width = 5, command = Three)
btn_four = Button(ui, text='4', width = 5, command = four)
btn_five = Button(ui, text='5', width = 5, command = five)
btn_six = Button(ui, text='6', width = 5, command = six)
btn_seven = Button(ui, text='7', width = 5, command = seven)
btn_eight = Button(ui, text='8', width = 5, command = eight)
btn_nine = Button(ui, text='9', width = 5, command = nine)
btn_plus = Button(ui, text='+', width = 5, command = plus)
btn_minus = Button(ui, text='-', width = 5, command = minus)
btn_mult = Button(ui, text='*', width = 5, command = mult)
btn_div = Button(ui, text='/', width = 5, command = div)
btn_negative = Button(ui, text = '+/-', width = 5, command = negative)

#button grid
btn_my.grid(row = 1, column=0, pady = 3)#computer always think that 0 = one 1 = scond
btn_c.grid(row = 1, column= 1)
btn_CE.grid(row = 1, column= 2)
btn_e.grid(row = 1, column = 3)
btn_zero.grid(row = 5, column = 0)
btn_one.grid(row = 2, column = 0)
btn_Two.grid(row = 2, column = 1)
btn_Three.grid(row = 2, column = 2)
btn_four.grid(row = 3, column = 0)
btn_five.grid(row = 3, column = 1)
btn_six.grid(row = 3, column = 2)
btn_seven.grid(row = 4, column = 0)
btn_eight.grid(row = 4, column = 1)
btn_nine.grid(row = 4, column = 2)
btn_plus.grid(row = 2, column = 3)
btn_minus.grid(row = 3, column = 3)
btn_mult.grid(row = 4, column = 3)
btn_div.grid(row = 5, column = 3)
btn_negative.grid(row = 5, column = 1)
ui.mainloop() # continuously loop