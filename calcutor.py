import tkinter
from tkinter import *
import re

root = Tk()
root.title("Calculator")
root.geometry("510x600+100+200")
root.configure(bg='black')
root.resizable(False, False)

label = Label(root, text="", width=400, height=2, bg="#fff", font=('arial', 30))
label.pack()

button_width = 4
button_height = 1
button_font = ('arial', 30)
x_offset = 10
y_offset = 130
button_gap = 130
row_gap = 90

equation = ""

def clear():
    global equation
    equation = ""
    label.config(text=equation)

def show(value):
    global equation
    if(value in ['+', '-', '*', '%', '/']):
        if len(equation):
            if equation[-1] in ["+", '-', '*', '/', '%']:
                return
    equation += value
    label.config(text=equation)

def pop():
    global equation
    if(len(equation)):
        equation = equation[:-1]
        label.config(text=equation)

def answer():
    global equation
    ans = 0
    if len(equation) and (equation[0] in ['/','%','*'] or equation[-1] in ['/','+','-','*']):
        equation = ""
        label.config(text=equation)
        return

    if len(set(re.findall(r'[+\-*/%]', equation))) > 1:
        equation = "আমি এখনো বাচ্চা, বড় হলে পারব। এটা সলভ করতে !"
        label.config(text=equation, font=('arial', 16), height=3)
        return

    if '+' in equation:
        operands = equation.split('+')
        ans = sum(float(i) for i in operands)

    elif '-' in equation:
        operands = equation.split('-')
        ans = float(operands[0])
        for i in operands[1:]:
            ans -= float(i)
    elif '*' in equation:
        ans = 1
        operands = equation.split('*')
        for num in operands:
            ans *= float(num)
    elif '/' in equation:
        operands = equation.split('/')
        ans = float(operands[0])
        for num in operands[1:]:
            if(int(num)==0):
                ans="Can not divided by zero"
            else:
                ans /= float(num)
    elif '%' in equation:
        ans=0
        operands=equation.split('%')
        operands.remove('')
        print(operands)
        num=operands[0]
        ans=float(num)/100.00


    equation = str(ans)
    label.config(text=equation)

Button(root, text='C', bg='#f78e2b', fg='white', font=button_font, width=button_width, height=button_height, command=lambda: clear()).place(x=x_offset, y=y_offset)
Button(root, text='%', bg='#f78e2b', fg='white', font=button_font, width=button_width, height=button_height, command=lambda: show("%")).place(x=x_offset + button_gap, y=y_offset)
Button(root, text='*', bg='#f78e2b', fg='white', font=button_font, width=button_width, height=button_height, command=lambda: show("*")).place(x=x_offset + 2 * button_gap, y=y_offset)
Button(root, text='/', bg='#f78e2b', fg='white', font=button_font, width=button_width, height=button_height, command=lambda: show('/')).place(x=x_offset + 3 * button_gap, y=y_offset)

y_offset += row_gap
Button(root, text='7', bg='#575454', fg='white', font=button_font, width=button_width, height=button_height, command=lambda: show("7")).place(x=x_offset, y=y_offset)
Button(root, text='8', bg='#575454', fg='white', font=button_font, width=button_width, height=button_height, command=lambda: show('8')).place(x=x_offset + button_gap, y=y_offset)
Button(root, text='9', bg='#575454', fg='white', font=button_font, width=button_width, height=button_height, command=lambda: show('9')).place(x=x_offset + 2 * button_gap, y=y_offset)
Button(root, text='+', bg='#f78e2b', fg='white', font=button_font, width=button_width, height=button_height, command=lambda: show('+')).place(x=x_offset + 3 * button_gap, y=y_offset)

y_offset += row_gap
Button(root, text='4', bg='#575454', fg='white', font=button_font, width=button_width, height=button_height, command=lambda: show('4')).place(x=x_offset, y=y_offset)
Button(root, text='5', bg='#575454', fg='white', font=button_font, width=button_width, height=button_height, command=lambda: show('5')).place(x=x_offset + button_gap, y=y_offset)
Button(root, text='6', bg='#575454', fg='white', font=button_font, width=button_width, height=button_height, command=lambda: show('6')).place(x=x_offset + 2 * button_gap, y=y_offset)
Button(root, text='-', bg='#f78e2b', fg='white', font=button_font, width=button_width, height=button_height, command=lambda: show('-')).place(x=x_offset + 3 * button_gap, y=y_offset)

y_offset += row_gap
Button(root, text='3', bg='#575454', fg='white', font=button_font, width=button_width, height=button_height, command=lambda: show('3')).place(x=x_offset, y=y_offset)
Button(root, text='2', bg='#575454', fg='white', font=button_font, width=button_width, height=button_height, command=lambda: show('2')).place(x=x_offset + button_gap, y=y_offset)
Button(root, text='1', bg='#575454', fg='white', font=button_font, width=button_width, height=button_height, command=lambda: show('1')).place(x=x_offset + 2 * button_gap, y=y_offset)
Button(root, text='=', bg='#5f758e', fg='white', font=button_font, width=button_width, height=button_height + 2, command=lambda: answer()).place(x=x_offset + 3 * button_gap, y=y_offset)

y_offset += row_gap
Button(root, text='0', bg='#575454', fg='white', font=button_font, width=button_width, height=button_height, command=lambda: show('0')).place(x=x_offset, y=y_offset)
Button(root, text='.', bg='#575454', fg='white', font=button_font, width=button_width, height=button_height, command=lambda: show('.')).place(x=x_offset + button_gap, y=y_offset)
Button(root, text='x', bg='red', fg='white', font=button_font, width=button_width, height=button_height, command=lambda: pop()).place(x=x_offset + 2 * button_gap, y=y_offset)

root.mainloop()
