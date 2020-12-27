from tkinter import *
expression = ""


def press(num):
   global expression
   expression = expression + str(num)
   equation.set(expression)


# def percentage(num1, num2):
#    global  expression
#    expression = 100 * float(num1)/float(num2)
#
#    expression = ""


def equal_press():
   try:
      global expression
      total = str(eval(expression))
      equation.set(total)
      expression = ""
   except:
      equation.set(" error ")
      expression = ""


def clear():
   global expression
   expression = ""
   equation.set("")


calk = Tk()
calk.configure(background="Grey")
calk.title("Калькулятор")
calk.geometry("350x290")
equation = StringVar()
expression_field = Entry(calk, textvariable=equation)
expression_field.grid(columnspan=100, ipadx=60)
equation.set('0')

clear_button = Button(calk, text=' AC ', command=clear, height=3, width=7)
clear_button.grid(row=2, column=0)

plus_minus = Button(calk, text=' ± ', height=3, width=7)
plus_minus.grid(row=2, column=1)

percent = Button(calk, text=' % ', height=3, width=7)
percent.grid(row=2, column=2)

button7 = Button(calk, text=' 7 ', command=lambda: press(7), height=3, width=7)
button7.grid(row=3, column=0)

button8 = Button(calk, text=' 8 ', command=lambda: press(8), height=3, width=7)
button8.grid(row=3, column=1)

button9 = Button(calk, text=' 9 ', command=lambda: press(9), height=3, width=7)
button9.grid(row=3, column=2)

button4 = Button(calk, text=' 4 ', command=lambda: press(4), height=3, width=7)
button4.grid(row=4, column=0)

button5 = Button(calk, text=' 5 ', command=lambda: press(5), height=3, width=7)
button5.grid(row=4, column=1)

button6 = Button(calk, text=' 6 ', command=lambda: press(6), height=3, width=7)
button6.grid(row=4, column=2)

button1 = Button(calk, text=' 1 ', command=lambda: press(1), height=3, width=7)
button1.grid(row=5, column=0)

divide = Button(calk, text=' ÷ ', command=lambda: press("/"), height=3, width=7)
divide.grid(row=2, column=3)

multiply = Button(calk, text=' X ', command=lambda: press("*"), height=3, width=7)
multiply.grid(row=3, column=3)

minus = Button(calk, text=' - ', command=lambda: press("-"), height=3, width=7)
minus.grid(row=4, column=3)

plus = Button(calk, text=' + ', command=lambda: press("+"), height=3, width=7)
plus.grid(row=5, column=3)

button3 = Button(calk, text=' 3 ', command=lambda: press(3), height=3, width=7)
button3.grid(row=5, column=2)

button2 = Button(calk, text=' 2 ', command=lambda: press(2), height=3, width=7)
button2.grid(row=5, column=1)

button0 = Button(calk, text=' 0 ', command=lambda: press(0), height=3, width=14)
button0.grid(row=6, column=0, columnspan=2)

Decimal = Button(calk, text='.', command=lambda: press('.'), height=3, width=7)
Decimal.grid(row=6, column=2)

equal = Button(calk, text=' = ', command=equal_press, height=3, width=7)
equal.grid(row=6, column=3)

calk.mainloop()
