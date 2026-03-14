import tkinter as tk
from tkinter.constants import DISABLED, ACTIVE

from PIL import ImageTk , Image

root = tk.Tk()
root.geometry("1920x1080")

my_img1 = ImageTk.PhotoImage(Image.open("/home/subhan/PycharmProjects/Subhan_SoftwareConstruction_Repo/images/1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("/home/subhan/PycharmProjects/Subhan_SoftwareConstruction_Repo/images/2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("/home/subhan/PycharmProjects/Subhan_SoftwareConstruction_Repo/images/3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("/home/subhan/PycharmProjects/Subhan_SoftwareConstruction_Repo/images/4.png"))

my_label = tk.Label(root,image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

image_list = [my_img1,my_img2,my_img3,my_img4]

# Functions
def forward_clicked(image_number):

    my_label.configure(image=image_list[image_number-1])
    button_forward.configure(command=lambda : forward_clicked(image_number+1))
    button_back.configure(command=lambda : back_clicked(image_number-1),state=ACTIVE)
    # Checking if it is last image
    if image_number == 4:
        button_forward.configure(state=DISABLED)

def end_clicked():
    root.quit()

def back_clicked(image_number):
    my_label.configure(image=image_list[image_number-1])
    button_back.configure(command=lambda : back_clicked(image_number-1))
    button_forward.configure(command=lambda : forward_clicked(image_number+1))

    # Checking if it is last image
    if image_number == 1:
        button_back.configure(state=DISABLED)


# Creating Buttons
button_back = tk.Button(root,text="<<",state=DISABLED)
button_end = tk.Button(root,text="Exit Program",command=end_clicked)
button_forward = tk.Button(root,text=">>",command=lambda: forward_clicked(2))

# Putting Buttons on Screen
button_back.grid(row=1,column=0)
button_end.grid(row=1,column=1)
button_forward.grid(row=1,column=2)

root.mainloop()