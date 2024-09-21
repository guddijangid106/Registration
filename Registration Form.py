import tkinter as tk
from tkinter import messagebox, ttk
import re
from datetime import datetime
from tkinter import simpledialog

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def password_strength(password):
    if len(password) < 6:
        return "Weak"
    elif len(password) < 10:
        return "Moderate"
    else:
        return "Strong"

def register():
    username = username_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    age = age_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    gender = gender_combobox.get()
    dob = dob_entry.get()

    if not username or not password or not email or not age or not phone or not address or not gender or not dob:
        messagebox.showerror("Error", "All fields must be filled out.")
        return

    if not validate_email(email):
        messagebox.showerror("Error", "Please enter a valid email address.")
        return

    if not age.isdigit() or int(age) <= 0:
        messagebox.showerror("Error", "Please enter a valid age.")
        return

    if not phone.isdigit() or len(phone) != 10:
        messagebox.showerror("Error", "Please enter a valid 10-digit phone number.")
        return

    # Show password strength
    strength = password_strength(password)
    messagebox.showinfo("Registration Successful", f"Username: {username}\nEmail: {email}\nAge: {age}\nPhone: {phone}\nAddress: {address}\nGender: {gender}\nDOB: {dob}\nPassword Strength: {strength}")

def reset_form():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    gender_combobox.set('')
    dob_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("350x450")

# Create labels and entries using grid layout
tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Age:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
age_entry = tk.Entry(root)
age_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Phone:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
phone_entry = tk.Entry(root)
phone_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Address:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
address_entry = tk.Entry(root)
address_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Gender:").grid(row=6, column=0, padx=10, pady=5, sticky="e")
gender_combobox = ttk.Combobox(root, values=["Male", "Female", "Other"])
gender_combobox.grid(row=6, column=1, padx=10, pady=5)

tk.Label(root, text="Date of Birth:").grid(row=7, column=0, padx=10, pady=5, sticky="e")
dob_entry = tk.Entry(root)
dob_entry.grid(row=7, column=1, padx=10, pady=5)

# Create buttons
submit_button = tk.Button(root, text="Register", command=register)
submit_button.grid(row=8, column=0, padx=10, pady=10)

reset_button = tk.Button(root, text="Reset", command=reset_form)
reset_button.grid(row=8, column=1, padx=10, pady=10)

# Start the main loop
root.mainloop()
