import tkinter as tk

root = tk.Tk()
root.title("Calculator")

icon = tk.PhotoImage(file='/home/subhan/Desktop/calculator_3534.png')
root.iconphoto(True,icon)


main_entry_field = tk.Entry(root,width=35,borderwidth=10)
main_entry_field.grid(row=0,column=0,columnspan=3)

def button_click(number):
    current = main_entry_field.get()
    main_entry_field.delete(0,tk.END)
    main_entry_field.insert(0,str(current) + str(number))

def button_clear_click():
    main_entry_field.delete(0,tk.END)

def button_add():
    global firstNumber
    global op
    op = "+"
    firstNumber = main_entry_field.get()
    main_entry_field.delete(0,tk.END)

def button_sub_click():
    global firstNumber
    global op
    op = "-"
    firstNumber = main_entry_field.get()
    main_entry_field.delete(0,tk.END)

def button_mult_click():
    global firstNumber
    global op
    op = "*"
    firstNumber = main_entry_field.get()
    main_entry_field.delete(0,tk.END)

def button_divide_click():
    global firstNumber
    global op
    op = "/"
    firstNumber = main_entry_field.get()
    main_entry_field.delete(0,tk.END)

def button_equal_click():
    secondNumber = main_entry_field.get()
    main_entry_field.delete(0,tk.END)

    match op:
        case "+":
            main_entry_field.insert(0,int(firstNumber) + int(secondNumber))
        case "-":
            main_entry_field.insert(0, int(firstNumber) - int(secondNumber))
        case "*":
            main_entry_field.insert(0, int(firstNumber) * int(secondNumber))
        case "/":
            main_entry_field.insert(0, int(firstNumber) / int(secondNumber))


# Creating Buttons
button_1 = tk.Button(root,padx=40,pady=40,text="1",command=lambda: button_click(1))
button_2 = tk.Button(root,padx=40,pady=40,text="2",command=lambda: button_click(2))
button_3 = tk.Button(root,padx=40,pady=40,text="3",command=lambda: button_click(3))

button_4 = tk.Button(root,padx=40,pady=40,text="4",command=lambda: button_click(4))
button_5 = tk.Button(root,padx=40,pady=40,text="5",command=lambda: button_click(5))
button_6 = tk.Button(root,padx=40,pady=40,text="6",command=lambda: button_click(6))

button_7 = tk.Button(root,padx=40,pady=40,text="7",command=lambda: button_click(7))
button_8 = tk.Button(root,padx=40,pady=40,text="8",command=lambda: button_click(8))
button_9 = tk.Button(root,padx=40,pady=40,text="9",command=lambda: button_click(9))

button_0 = tk.Button(root,padx=40,pady=40,text="0",command=lambda: button_click(0))

button_clear = tk.Button(root,padx=79,pady=40,text="clear",command=button_clear_click,bg="cyan",fg="black")

button_add = tk.Button(root,padx=40,pady=40,text="+",command=button_add)

button_equal = tk.Button(root,padx=90,pady=40,text="=",command=button_equal_click,bg="cyan",fg="black")

button_sub = tk.Button(root,padx=40,pady=40,text="-",command=button_sub_click)
button_mult = tk.Button(root,padx=40,pady=40,text="*",command=button_mult_click)
button_divide = tk.Button(root,padx=40,pady=40,text="/",command=button_divide_click)

# Putting Buttons on screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)

button_clear.grid(row=4,column=1,columnspan=2)

button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)

button_sub.grid(row=6,column=0)
button_mult.grid(row=6,column=1)
button_divide.grid(row=6,column=2)

tk.mainloop()