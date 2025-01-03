import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.title("User Account Information")
root.attributes("-fullscreen", True)
root.configure(bg="lightblue")  # Set entire background to light blue

image_path = "C:\\Users\\JAYSON RAMIREZ\\Downloads\\lyone.png"
image = Image.open(image_path)
image = image.resize((150, 150))
photo = ImageTk.PhotoImage(image)

header = tk.Label(
    root,
    text="USER ACCOUNT INFORMATION",
    font=("Arial", 24, "bold"),
    bg="lightblue",
    fg="white"
)
header.pack(pady=20)

profile_frame = tk.Frame(root, bg="lightgray", relief="solid", bd=1)
profile_frame.place(x=30, y=100, width=220, height=250)

profile_label = tk.Label(profile_frame, bg="white", width=150, height=150, relief="ridge")
profile_label.pack(pady=10)

upload_button = tk.Button(
    profile_frame,
    text="Upload Picture",
    font=("Arial", 12),
    bg="blue",
    fg="white",
)
upload_button.pack(pady=10)

# Form Section
form_frame = tk.Frame(root, bg="lightgray", padx=20, pady=20, relief="solid", bd=1)
form_frame.place(x=280, y=100, width=1000, height=700)

form_title = tk.Label(
    form_frame,
    text="User Information",
    font=("Arial", 20, "bold"),
    bg="lightgray",
    fg="black"
)
form_title.grid(row=0, column=0, columnspan=2, pady=10)

fields = [
    "First Name", "Middle Name", "Last Name", "Department", "Designation",
    "Username", "Password", "Confirm Password", "User Type", "User Status", "Employee Number"
]
entries = {}

# Using grid layout for form fields
for idx, field in enumerate(fields):
    field_label = tk.Label(
        form_frame,
        text=f"{field}:",
        font=("Arial", 14),
        bg="lightgray",
        fg="black"
    )
    field_label.grid(row=idx + 1, column=0, sticky="w", pady=5, padx=10)

    entry = tk.Entry(
        form_frame,
        width=50,
        bg="white",
        fg="black",
        font=("Arial", 14)
    )
    entry.grid(row=idx + 1, column=1, pady=5, padx=10)
    entries[field] = entry

# Options Buttons Section
options_frame = tk.Frame(root, bg="lightblue")
options_frame.place(relx=0.5, rely=0.9, anchor="center", width=800, height=80)

update_profile_button = tk.Button(
    options_frame,
    text="Update Profile",
    width=15,
    bg="green",
    fg="white",
    font=("Arial", 14, "bold")
)
update_profile_button.grid(row=0, column=0, padx=20, pady=10)

delete_profile_button = tk.Button(
    options_frame,
    text="Delete Profile",
    width=15,
    bg="red",
    fg="white",
    font=("Arial", 14, "bold")
)
delete_profile_button.grid(row=0, column=1, padx=20, pady=10)

cancel_button = tk.Button(
    options_frame,
    text="Cancel",
    width=15,
    bg="blue",
    fg="white",
    font=("Arial", 14, "bold")
)
cancel_button.grid(row=0, column=2, padx=20, pady=10)

footer = tk.Label(
    root,
    text="© 2025 User Management System",
    font=("Arial", 12),
    bg="lightblue",
    fg="black"
)
footer.pack(side="bottom", pady=20)

root.mainloop()
