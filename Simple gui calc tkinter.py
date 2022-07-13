# Python program to create a simple ken
# calculator using Tkinter
 
# import everything from tkinter module
from tkinter import *
 
# globally declare the my_function variable
my_function = ""
 
 
# Function to update my_function
# in the text entry box
def press(num):
    # point out the global my_function variable
    global my_function
 
    # concatenation of string
    my_function = my_function + str(num)
 
    # update the my_function by using set method
    equation.set(my_function)
 
 
# Function to evaluate the final my_function
def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.
 
    # Put that code inside the try block
    # which may generate the error
    try:
 
        global my_function
 
        # eval function evaluate the my_function
        # and str function convert the result
        # into string
        total = str(eval(my_function))
 
        equation.set(total)
 
        # initialize the my_function variable
        # by empty string
        my_function = ""
 
    # if error is generate then handle
    # by the except block
    except:
 
        equation.set(" error ")
        my_function = ""
 
 
# Function to clear the contents
# of text entry box
def clear():
    global my_function
    my_function = ""
    equation.set("")
 
 
# Driver code
    # create a ken window
ken = Tk()
 
    # set the background colour of ken window
ken.configure(background="light green")
 
    # set the title of ken window
ken.title("Simple Calculator")
 
    # set the configuration of ken window
ken.geometry("270x150")
 
    # StringVar() is the variable class
    # we create an instance of this class
equation = StringVar()
 
    # create the text entry box for
    # showing the my_function .
my_function_field = Entry(ken, textvariable=equation)
 
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
my_function_field.grid(columnspan=4, ipadx=70)
 
    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
button1 = Button(ken, text=' 1 ', fg='black', bg='red',
                    command=lambda: press(1), height=1, width=7)
button1.grid(row=2, column=0)
 
button2 = Button(ken, text=' 2 ', fg='black', bg='red',
                    command=lambda: press(2), height=1, width=7)
button2.grid(row=2, column=1)
 
button3 = Button(ken, text=' 3 ', fg='black', bg='red',
                    command=lambda: press(3), height=1, width=7)
button3.grid(row=2, column=2)
button4 = Button(ken, text=' 4 ', fg='black', bg='red',
                    command=lambda: press(4), height=1, width=7)
button4.grid(row=3, column=0)
button5 = Button(ken, text=' 5 ', fg='black', bg='red',
                    command=lambda: press(5), height=1, width=7)
button5.grid(row=3, column=1)
 
button6 = Button(ken, text=' 6 ', fg='black', bg='red',
                    command=lambda: press(6), height=1, width=7)
button6.grid(row=3, column=2)
 
button7 = Button(ken, text=' 7 ', fg='black', bg='red',
                    command=lambda: press(7), height=1, width=7)
button7.grid(row=4, column=0)
 
button8 = Button(ken, text=' 8 ', fg='black', bg='red',
                    command=lambda: press(8), height=1, width=7)
button8.grid(row=4, column=1)
 
button9 = Button(ken, text=' 9 ', fg='black', bg='red',
                    command=lambda: press(9), height=1, width=7)
button9.grid(row=4, column=2)
 
button0 = Button(ken, text=' 0 ', fg='black', bg='red',
                    command=lambda: press(0), height=1, width=7)
button0.grid(row=5, column=0)
 
plus = Button(ken, text=' + ', fg='black', bg='red',
                command=lambda: press("+"), height=1, width=7)
plus.grid(row=2, column=3)
 
minus = Button(ken, text=' - ', fg='black', bg='red',
                command=lambda: press("-"), height=1, width=7)
minus.grid(row=3, column=3)
 
multiply = Button(ken, text=' * ', fg='black', bg='red',
                    command=lambda: press("*"), height=1, width=7)
multiply.grid(row=4, column=3)
 
divide = Button(ken, text=' / ', fg='black', bg='red',
                    command=lambda: press("/"), height=1, width=7)
divide.grid(row=5, column=3)
 
equal = Button(ken, text=' = ', fg='black', bg='red',
                command=equalpress, height=1, width=7)
equal.grid(row=5, column=2)
 
clear = Button(ken, text='Clear', fg='black', bg='red',
                command=clear, height=1, width=7)
clear.grid(row=5, column='1')
 
Decimal= Button(ken, text='.', fg='black', bg='red',
                    command=lambda: press('.'), height=1, width=7)
Decimal.grid(row=6, column=0)
    # start the ken
ken.mainloop()
