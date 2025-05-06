import tkinter as tk
from tkinter import messagebox

# Sample credentials for testing
VALID_USERNAME = "admin"
VALID_PASSWORD = "12345"

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# GUI Window
window = tk.Tk()
window.title("Sign In")
window.geometry("300x200")
window.resizable(False, False)

# Username Label and Entry
tk.Label(window, text="Username:").pack(pady=(10, 0))
entry_username = tk.Entry(window, width=30)
entry_username.pack()

# Password Label and Entry
tk.Label(window, text="Password:").pack(pady=(10, 0))
entry_password = tk.Entry(window, width=30, show="*")
entry_password.pack()

# Sign In Button
tk.Button(window, text="Sign In", command=login).pack(pady=20)

window.mainloop()