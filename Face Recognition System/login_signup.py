import os
import subprocess
import tkinter as tk
from tkinter import messagebox

# Dummy database for demonstration (replace this with your actual user database)
users = {"anul": "shrestha"}

# Function to handle login button click
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if the username and password match the records
    if username in users and users[username] == password:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        root.destroy()  # Close the login window
        open_ui_interface(username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function to handle signup button click
def signup():
    # Create a new window for signup
    signup_window = tk.Toplevel(root)
    signup_window.title("Signup")

    # Create labels and entry fields for username and password
    signup_username_label = tk.Label(signup_window, text="Username:")
    signup_username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
    signup_username_entry = tk.Entry(signup_window)
    signup_username_entry.grid(row=0, column=1, padx=10, pady=5)

    signup_password_label = tk.Label(signup_window, text="Password:")
    signup_password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
    signup_password_entry = tk.Entry(signup_window, show="*")
    signup_password_entry.grid(row=1, column=1, padx=10, pady=5)

    # Function to handle signup confirmation
    def confirm_signup():
        new_username = signup_username_entry.get()
        new_password = signup_password_entry.get()

        # Add the new user to the database (replace this with your actual user registration process)
        users[new_username] = new_password
        messagebox.showinfo("Signup Successful", "Account created successfully!")
        signup_window.destroy()

    # Create a signup button in the signup window
    signup_button = tk.Button(signup_window, text="Signup", command=confirm_signup)
    signup_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Function to open the UI interface
def open_ui_interface(username):
    os.system('python UI.py')

# Create the main application window
root = tk.Tk()
root.title("Login")

# Create labels and entry fields for username and password
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Create login and signup buttons
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

signup_button = tk.Button(root, text="Signup", command=signup)
signup_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

# Run the application
root.mainloop()
