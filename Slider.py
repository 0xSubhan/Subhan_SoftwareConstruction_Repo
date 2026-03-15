import tkinter as tk

window = tk.Tk()

window.title("My GUI")

window.geometry("600x400")

def slide(number):
    window.geometry(str(number)+"x400")

vertical = tk.Scale(window,from_=0,to=400,command=lambda value : slide(value))
vertical.pack()






window.mainloop()