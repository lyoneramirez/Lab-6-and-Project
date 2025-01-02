import tkinter as tk
from tkinter import messagebox

def handle_login():
    username = username_entry.get()
    password = password_entry.get()

    # Simulate login validation
    if username == "lyone" and password == "password123":
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password!")

# Create the main application window
root = tk.Tk()
root.title("LPU Cavite Login")
root.geometry("600x400")
root.configure(bg="#ffffff")

# Header Section
header_frame = tk.Frame(root, bg="#ffffff")
header_frame.pack(fill="x", pady=20)

tk.Label(
    header_frame,
    text="LYCEUM OF THE PHILIPPINES UNIVERSITY",
    font=("Arial", 16, "bold"),
    bg="#ffffff",
    fg="#800000"
).pack()

tk.Label(
    header_frame,
    text="CAVITE",
    font=("Arial", 14, "bold"),
    bg="#ffffff",
    fg="#800000"
).pack()

# Login Form Section
login_frame = tk.Frame(root, bg="#ffffff")
login_frame.pack(pady=40)

tk.Label(
    login_frame,
    text="Login to Your Account",
    font=("Arial", 14, "bold"),
    bg="#ffffff",
    fg="#800000"
).pack(pady=10)

# Username Field
tk.Label(
    login_frame,
    text="Username:",
    font=("Arial", 12),
    bg="#ffffff",
    fg="#000000"
).pack(anchor="w", padx=10)
username_entry = tk.Entry(login_frame, font=("Arial", 12), width=30, bg="#f8f8f8")
username_entry.pack(pady=5)

tk.Label(
    login_frame,
    text="Password:",
    font=("Arial", 12),
    bg="#ffffff",
    fg="#000000"
).pack(anchor="w", padx=10)
password_entry = tk.Entry(login_frame, font=("Arial", 12), width=30, bg="#f8f8f8", show="*")
password_entry.pack(pady=5)

login_button = tk.Button(
    login_frame,
    text="Login",
    font=("Arial", 12, "bold"),
    bg="#800000",
    fg="#ffffff",
    width=15,
    command=handle_login
)
login_button.pack(pady=20)

root.mainloop()
