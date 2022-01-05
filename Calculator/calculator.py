
from tkinter import *
 


expression = ""
 
 

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
 

def equalpress():
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
 
 
if __name__ == "__main__":
    root = Tk()
    root.configure(background="Grey")
    root.title("Calculator By Prabisha")
 
    root.geometry("310x510")
 
    equation = StringVar()

    input_field = Entry(root, textvariable=equation)
    input_field.grid(row=0, column=0, columnspan=3, padx=30, pady=20)
 
    
    button1 = Button(root, text=' 1 ', fg='black', bg="grey",command=lambda: press(1), padx=40, pady=20)
    button1.grid(row=3, column=0)
 
    button2 = Button(root, text=' 2 ', fg='black', bg='grey', command=lambda: press(2), padx=40, pady=20)
    button2.grid(row=3, column=1)
 
    button3 = Button(root, text=' 3 ', fg='black', bg='grey', command=lambda: press(3), padx=40, pady=20)
    button3.grid(row=3, column=2)
 
    button4 = Button(root, text=' 4 ', fg='black', bg='grey', command=lambda: press(4),padx=40, pady=20)
    button4.grid(row=2, column=0)
 
    button5 = Button(root, text=' 5 ', fg='black', bg='grey', command=lambda: press(5), padx=40, pady=20)
    button5.grid(row=2, column=1)
 
    button6 = Button(root, text=' 6 ', fg='black', bg='grey',command=lambda: press(6), padx=40, pady=20)
    button6.grid(row=2, column=2)
 
    button7 = Button(root, text=' 7 ', fg='black', bg='grey', command=lambda: press(7),padx=40, pady=20)
    button7.grid(row=1, column=0)
 
    button8 = Button(root, text=' 8 ', fg='black', bg='grey', command=lambda: press(8),padx=40, pady=20)
    button8.grid(row=1, column=1)
 
    button9 = Button(root, text=' 9 ', fg='black', bg='grey', command=lambda: press(9), padx=40, pady=20)
    button9.grid(row=1, column=2)
 
    button0 = Button(root, text=' 0 ', fg='black', bg='grey', command=lambda: press(0), padx=40, pady=20)
    button0.grid(row=4, column=1)
 
    plus = Button(root, text=' + ', fg='black', bg='grey', command=lambda: press("+"), padx=40, pady=20)
    plus.grid(row=4, column=0)
 
    minus = Button(root, text=' - ', fg='black', bg='grey',command=lambda: press("-"), padx=40, pady=20)
    minus.grid(row=4, column=2)
 
    multiply = Button(root, text=' * ', fg='black', bg='grey',command=lambda: press("*"), padx=40, pady=20)
    multiply.grid(row=5, column=0)
 
    divide = Button(root, text=' / ', fg='black', bg='grey', command=lambda: press("/"), padx=40, pady=20)
    divide.grid(row=6, column=0)
 
    equal = Button(root, text=' = ', fg='black', bg='grey', command=equalpress, padx=89, pady=20)
    equal.grid(row=6, column=1, columnspan=2)
 
    clear = Button(root, text='Clear', fg='black', bg='grey', command=clear, padx=85, pady=20)
    clear.grid(row=5, column=1, columnspan = 2)
 
    
    
    root.mainloop()