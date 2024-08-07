
from system.app import *


import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    item_name = item_name_entry.get()
    customer_name = customer_name_entry.get()
    gw = gw_entry.get()
    gender = gender_var.get()
    
    if not item_name or not customer_name or not gw:
        messagebox.showwarning("Input Error", "All fields are required!")
        return
    
    messagebox.showinfo("Form Submitted", f"item_name: {item_name}\ncustomer_name: {customer_name}\ngw: {gw}\nGender: {gender}")
    sellItem(item_name,customer_name,gw)
# Create the main window
root = tk.Tk()
root.title("ShopManager")
intializing()
# Create and place widgets
tk.Label(root, text="item_name:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
item_name_entry = tk.Entry(root)
item_name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="customer_name:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
customer_name_entry = tk.Entry(root)
customer_name_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="gw:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
gw_entry = tk.Entry(root)
gw_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Gender:").grid(row=3, column=0, padx=10, pady=5, sticky='e')
gender_var = tk.StringVar(value='Not Specified')
tk.Radiobutton(root, text="Male", variable=gender_var, value='Male').grid(row=3, column=1, padx=10, pady=5, sticky='w')
tk.Radiobutton(root, text="Female", variable=gender_var, value='Female').grid(row=4, column=1, padx=10, pady=5, sticky='w')

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()
