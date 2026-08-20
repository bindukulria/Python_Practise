import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("Course Selection")
root.geometry("300x200")

courses={"C":3500,"C++":500}

def show_price(event):
    selected=combo.get()
    price=courses[selected]
    Label.config(text="Price:"+ str(price))

combo=ttk.Combobox(root,
values=list(courses.keys()),
state="readonly")

combo.pack(pady=30)
combo.bind("<<ComboboxSelected>>",
show_price)

Label=tk.Label(root,text="Price:")
Label.pack()

root.mainloop()
