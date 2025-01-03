import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Payroll System Login")
root.geometry("400x300")
root.configure(bg="white")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (400 / 2))
y_coordinate = int((screen_height / 2) - (300 / 2))
root.geometry(f"400x300+{x_coordinate}+{y_coordinate}")

header = tk.Label(root, text="LOGIN", font=("Arial", 20, "bold"), bg="white", fg="darkblue")
header.pack(pady=20)

username_label = tk.Label(root, text="Username:", font=("Arial", 12), bg="white", fg="black")
username_label.pack(anchor="w", padx=40)
username_entry = tk.Entry(root, font=("Arial", 12), width=30)
username_entry.pack(pady=5)

password_label = tk.Label(root, text="Password:", font=("Arial", 12), bg="white", fg="black")
password_label.pack(anchor="w", padx=40)
password_entry = tk.Entry(root, font=("Arial", 12), width=30, show="*")
password_entry.pack(pady=5)

def handle_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome to the Payroll System!")
        root.destroy()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password!")

login_button = tk.Button(
    root,
    text="Login",
    font=("Arial", 12, "bold"),
    bg="cornflowerblue",
    fg="white",
    width=15,
    command=handle_login
)
login_button.pack(pady=20)

footer = tk.Label(root, text="© Ramirez Payroll System", font=("Arial", 10), bg="white", fg="gray")
footer.pack(side="bottom", pady=10)

root.mainloop()
