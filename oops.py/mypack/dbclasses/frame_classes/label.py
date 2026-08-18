from tkinter import *

root =Tk()
root.title("My Form")
root.geometry("400x300")
 
title=Label(root, text="Select Your Labels",font=("Arial",18))
title.pack(pady=20)

name_Label=Label(root, text="Name")
name_Label.pack()

email_Label=Label(root, text="Email")
email_Label.pack()

age_Label=Label(root, text="Age")
age_Label.pack()

root.mainloop()

