import tkinter as tk
from tkinter import ttk, messagebox

root=tk.Tk()
root.title("Country State City")
root.geometry("500x400")

countries=[
{"id":1,"name":"India"},
{"id":2,"name":"USA"}
]
states=[
{"id":1,"Country_id":1,"name":"Haryana"},
{"id":2,"Country_id":1,"name":"Punjab"},
{"id":6,"Country_id":2,"name":"Californai"}
]
cities=[
{"id":1,"state_id":1,"name":"Gurugram"},
{"id":2,"state_id":1,"name":"Faridabad"},
{"id":3,"state_id":2,"name":"Ludhiana"}
]

country_combo=ttk.Combobox(root,
state="readonly")
country_combo.pack(pady=10)

state_combo=ttk.Combobox(root,
state="readonly")
state_combo.pack(pady=10)

city_combo=ttk.Combobox(root,
state="readonly")
city_combo.pack(pady=10)

country_combo["values"]=["India","USA"]

def country_selected(event):
 country=country_combo.get()

if country_combo.get()=="India":
    state_combo["values"]=[
            "Haryana",
            "Punjab",
            "Rajasthan",
        ]
elif country_combo.get()=="USA":
        state_combo["values"]=[
            "Californai",
            "Texas",
            "Florida",
        ]
def state_selected(event):

    state=state_combo.get()
    if state=="Haryana":
        city_combo["values"]=[
            "Gurugram",
            "Faridada",
            "Panipat",
]
    elif state=="Panjab":
        city_combo["values"]=[
            "Ludhiana,"
            "Amritsar",
            "Jalandhar",
        ]
        country_combo.bind(
            "<<ComboboxSeleted>>",
            country_selected
        )
    state_combo.bind(
        "<<ComboboxSelectd>>",
        state_selected
    )

    root.mainloop()