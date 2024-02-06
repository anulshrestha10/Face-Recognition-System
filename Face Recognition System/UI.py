import os
import tkinter as tk
from tkinter import Toplevel, messagebox


# Function to add a new user
def add_user():
    os.system('python add_faces.py')

# Function to delete a user
def delete_user():
    os.system('python delete_users.py')

# Function to show registered users
def show_users():
    os.system(' python show_users.py')

# Function to open 'main.py' for taking attendance
def take_attendance():
    os.system('python main.py')

# Create the main application window
root = tk.Tk()
root.title("User Management System")

# Configure colors
bg_color = "#f0f0f0"
button_bg_color = "#4CAF50"
button_fg_color = "white"

# Configure padding
button_padding = 10

# Create buttons for each feature
add_button = tk.Button(root, text="Add User", command=add_user, bg=button_bg_color, fg=button_fg_color, padx=button_padding)
add_button.pack(fill="x", padx=10, pady=(20, 5))

delete_button = tk.Button(root, text="Delete User", command=delete_user, bg=button_bg_color, fg=button_fg_color, padx=button_padding)
delete_button.pack(fill="x", padx=10, pady=5)

show_button = tk.Button(root, text="Show Registered Users", command=show_users, bg=button_bg_color, fg=button_fg_color, padx=button_padding)
show_button.pack(fill="x", padx=10, pady=5)

attendance_button = tk.Button(root, text="Take Attendance", command=take_attendance, bg=button_bg_color, fg=button_fg_color, padx=button_padding)
attendance_button.pack(fill="x", padx=10, pady=(5, 20))

# Set background color
root.configure(background=bg_color)

# Run the application
root.mainloop()
