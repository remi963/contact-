import tkinter as tk
from tkinter import messagebox
import csv


def save_contact():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    address = entry_address.get("1.0",tk.END).strip()

    if name and email and phone and address:  
        with open('contacts.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, email, phone, address])
        messagebox.showinfo("Success", "Contact saved successfully!")
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_address.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Error", "Please fill all fields!")

window = tk.Tk()
window.title("Contact Form")
window.geometry("300x400")

tk.Label(window, text="Name:").pack(pady=5)
entry_name = tk.Entry(window)
entry_name.pack()

tk.Label(window, text="Email:").pack(pady=5)
entry_email = tk.Entry(window)
entry_email.pack()

tk.Label(window, text="Phone:").pack(pady=5)
entry_phone = tk.Entry(window)
entry_phone.pack()

tk.Label(window, text="Address:").pack(pady=5)
entry_address = tk.Text(window, height=5, width=30)
entry_address.pack()


tk.Button(window, text="Save Contact", command=save_contact).pack(pady=20)


window.mainloop()