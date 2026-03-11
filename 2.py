import tkinter as tk

window = tk.Tk()
window.geometry('400x400')

label = tk.Label(window,text='Toggle Color')

def toggleColor():
    current_color = button.cget('bg')

    if current_color == 'red':
        current_color = 'green'
    else:
        current_color = 'red'

    button.configure(bg=current_color)

button = tk.Button(window,text='Click',command=toggleColor,padx=20,pady=20)
button.pack()

# Events

def handle_click(event):
    print(f'location X={event.x} , Y={event.y}')

def handle_key(event):
    print(f'Key  = {event.char}')

button = tk.Button(window,text='Button Location!')
button.pack()

entry = tk.Entry(window)
entry.pack()
# Ya bind kyu kiya ha , ya baad ma dekh lein! mera kiyal sa bind method ha button class ka, baad ma!
button.bind("<Button-1>",handle_click)
entry.bind("<Key>",handle_key)









window.mainloop()