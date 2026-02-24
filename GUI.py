import tkinter as tk


window = tk.Tk()

window.title("My GUI")

window.geometry("600x400")

label_userName = tk.Label(window,text="User Name",font=("Times New Roman",20),fg="black",bg="cyan")
label_userName.pack()


def take():
    input = entry.get()
    print("Data: ",input)



entry = tk.Entry(window,width=50)
entry.pack()

button = tk.Button(window,text="Submit",command=take)
button.pack()

window.mainloop()


