import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Employee Registration")
root.geometry("1000x1000")
root.configure(bg="#1a1a1a")

header = tk.Label(root, text="EMPLOYEE REGISTRATION", font=("Arial", 24, "bold"), bg="#1a1a1a", fg="#c1a3e8")
header.pack(pady=20)

info_frame = tk.Frame(root, bg="#2d2d2d", relief="solid", bd=1)
info_frame.place(x=20, y=80, width=960, height=800)

tk.Label(info_frame, text="Employee Information", font=("Arial", 18, "bold"), bg="#2d2d2d", fg="#ffffff").pack(pady=20)

def upload_picture():
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if filepath:
        img = Image.open(filepath)
        img = img.resize((150, 150), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        profile_picture_label.config(image=photo)
        profile_picture_label.image = photo

profile_picture_label = tk.Label(info_frame, bg="#2d2d2d", width=150, height=150, relief="ridge")
profile_picture_label.place(x=750, y=40)

upload_button = tk.Button(
    info_frame, text="Upload Picture", command=upload_picture, font=("Arial", 10), bg="#7f5fbf", fg="#ffffff"
)
upload_button.place(x=770, y=500)

fields = [
    "First Name",
    "Last Name",
    "Middle Name",
    "Date of Birth",
    "Gender",
    "Nationality",
    "Civil Status",
    "Department",
    "Designation",
    "Qualified Dependents Status",
    "Employee Status",
    "Paydate",
    "Employee Number",
    "Contact Number",
    "Email Address",
    "Social Media Account",
    "Full Address",
]
entries = {}

y_offset = 30
for i, field in enumerate(fields):
    x_offset = 30 if i % 2 == 0 else 500
    if i % 2 == 0 and i > 0:
        y_offset += 60

    tk.Label(info_frame, text=f"{field}:", font=("Arial", 14), bg="#2d2d2d", fg="#ffffff").place(x=x_offset, y=y_offset)
    entry = tk.Entry(info_frame, font=("Arial", 14), width=25)
    entry.place(x=x_offset + 200, y=y_offset)
    entries[field] = entry

def save_employee():
    employee_info = {field: entry.get() for field, entry in entries.items()}

    details = "\n".join([f"{key}: {value}" for key, value in employee_info.items()])
    messagebox.showinfo("Employee Registered", f"The following employee details have been saved:\n\n{details}")

    for entry in entries.values():
        entry.delete(0, tk.END)
    profile_picture_label.config(image="")
    profile_picture_label.image = None

save_button = tk.Button(
    root,
    text="Save Employee",
    font=("Arial", 14, "bold"),
    bg="#7f5fbf",
    fg="#ffffff",
    width=25,
    command=save_employee
)
save_button.place(x=650, y=650)

footer = tk.Label(root, text="© 2025 Employee Management System", font=("Arial", 12), bg="#1a1a1a", fg="#ffffff")
footer.pack(side="bottom", pady=10)

root.mainloop()