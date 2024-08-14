import tkinter as tk
from tkinter import messagebox

def register():
    username = username_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    
    # Here you can perform validation or additional checks
    
    # For simplicity, just displaying the entered data
    messagebox.showinfo("Registration Successful", f"Username: {username}\nEmail: {email}")

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create labels and entries for username, password, and email
username_label = tk.Label(root, text="Username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")  # show="*" to hide the password
password_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()

email_entry = tk.Entry(root)
email_entry.pack()

# Create a submit button
submit_button = tk.Button(root, text="Register", command=register)
submit_button.pack()

# Start the main loop
root.mainloop()
