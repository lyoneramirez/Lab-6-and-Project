import tkinter as tk
from tkinter import ttk

# Initialize the main window
root = tk.Tk()
root.title("Payroll System")
root.geometry("1024x768")  # Set the window size
root.configure(bg="white")

# Center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (1024 / 2))
y_coordinate = int((screen_height / 2) - (768 / 2))
root.geometry(f"1024x768+{x_coordinate}+{y_coordinate}")

# Header
header = tk.Label(root, text="PAYROLL SYSTEM", font=("Arial", 20, "bold"), bg="white", fg="darkblue")
header.pack(pady=10)

# Employee Basic Info Frame
basic_info_frame = tk.Frame(root, bg="lightblue", relief="solid", bd=1)
basic_info_frame.place(x=20, y=50, width=450, height=220)

tk.Label(basic_info_frame, text="EMPLOYEE BASIC INFO:", font=("Arial", 12, "bold"), bg="lightblue", fg="white").pack(anchor="w", padx=10, pady=5)
tk.Label(basic_info_frame, text="Employee Number:", bg="lightblue", fg="black").place(x=10, y=40)
emp_number = tk.Entry(basic_info_frame, width=30)
emp_number.place(x=180, y=40)

tk.Label(basic_info_frame, text="Search Employee:", bg="lightblue", fg="black").place(x=10, y=80)
search_emp = tk.Entry(basic_info_frame, width=25)
search_emp.place(x=180, y=80)

search_button = tk.Button(basic_info_frame, text="SEARCH", bg="darkblue", fg="white", font=("Arial", 10))
search_button.place(x=360, y=80)

tk.Label(basic_info_frame, text="Department:", bg="lightblue", fg="black").place(x=10, y=120)
department = tk.Entry(basic_info_frame, width=40)
department.place(x=180, y=120)

# Personal Information Frame
personal_info_frame = tk.Frame(root, bg="lightblue", relief="solid", bd=1)
personal_info_frame.place(x=500, y=50, width=500, height=220)

tk.Label(personal_info_frame, text="Personal Information:", font=("Arial", 12, "bold"), bg="lightblue", fg="white").pack(anchor="w", padx=10, pady=5)

fields = ["Firstname", "Middle Name", "Surname", "Civil Status", "Qualified Dependents Status", "Paydate", "Employee Status", "Designation"]
for i, field in enumerate(fields):
    tk.Label(personal_info_frame, text=f"{field}:", bg="lightblue", fg="black").place(x=10, y=30 + (i * 20))
    tk.Entry(personal_info_frame, width=35).place(x=220, y=30 + (i * 20))

# Basic Income Frame
income_frame = tk.Frame(root, bg="lightblue", relief="solid", bd=1)
income_frame.place(x=20, y=300, width=450, height=200)

tk.Label(income_frame, text="BASIC INCOME:", font=("Arial", 12, "bold"), bg="lightblue", fg="white").pack(anchor="w", padx=10, pady=5)
income_fields = ["Rate/Hour", "No. of Hours / Cut Off", "Income / Cut Off"]
for i, field in enumerate(income_fields):
    tk.Label(income_frame, text=f"{field}:", bg="lightblue", fg="black").place(x=10, y=40 + (i * 40))
    tk.Entry(income_frame, width=25).place(x=200, y=40 + (i * 40))

# Deductions Frame
deductions_frame = tk.Frame(root, bg="lightblue", relief="solid", bd=1)
deductions_frame.place(x=500, y=300, width=500, height=200)

tk.Label(deductions_frame, text="REGULAR DEDUCTIONS:", font=("Arial", 12, "bold"), bg="lightblue", fg="white").pack(anchor="w", padx=10, pady=5)
deduction_fields = ["SSS Contribution", "PhilHealth Contribution", "Pagibig Contribution", "Income Tax Contribution"]
for i, field in enumerate(deduction_fields):
    tk.Label(deductions_frame, text=f"{field}:", bg="lightblue", fg="black").place(x=10, y=40 + (i * 40))
    tk.Entry(deductions_frame, width=35).place(x=220, y=40 + (i * 40))

# Summary Frame
summary_frame = tk.Frame(root, bg="lightblue", relief="solid", bd=1)
summary_frame.place(x=20, y=520, width=980, height=120)

tk.Label(summary_frame, text="SUMMARY INCOME:", font=("Arial", 12, "bold"), bg="lightblue", fg="white").pack(anchor="w", padx=10, pady=5)
tk.Label(summary_frame, text="GROSS INCOME:", bg="lightblue", fg="black").place(x=10, y=40)
tk.Entry(summary_frame, width=20).place(x=150, y=40)

tk.Label(summary_frame, text="NET INCOME:", bg="lightblue", fg="black").place(x=400, y=40)
tk.Entry(summary_frame, width=20).place(x=550, y=40)

# Action Buttons
action_buttons = [("GROSS INCOME", "darkblue"), ("NET INCOME", "blue"), ("SAVE", "cornflowerblue"), ("UPDATE", "royalblue"), ("NEW", "steelblue")]
for idx, (text, color) in enumerate(action_buttons):
    tk.Button(root, text=text, bg=color, fg="white", width=15, font=("Arial", 12)).place(x=20 + (idx * 200), y=680)

# Run the main loop
root.mainloop()
