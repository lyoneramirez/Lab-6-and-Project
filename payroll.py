import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Se-Ri's Choice Payroll")
root.geometry("800x700")
root.configure(bg="light blue")


header = tk.Label(root, text="SE-RI'S CHOICE PAYROLL", font=("Arial", 20, "bold"), bg="light blue", fg="#000000")
header.pack(pady=10)


basic_info_frame = tk.Frame(root, bg="#ffffff", relief="solid", bd=1)
basic_info_frame.place(x=10, y=50, width=350, height=200)

tk.Label(basic_info_frame, text="EMPLOYEE BASIC INFO:", font=("Arial", 12, "bold"), bg="#ffffff").pack(anchor="w", padx=10, pady=5)
tk.Label(basic_info_frame, text="Employee Number:", bg="#ffffff").place(x=10, y=40)
emp_number = tk.Entry(basic_info_frame, width=20)
emp_number.place(x=150, y=40)

tk.Label(basic_info_frame, text="Search Employee:", bg="#ffffff").place(x=10, y=70)
search_emp = tk.Entry(basic_info_frame, width=15)
search_emp.place(x=150, y=70)

search_button = tk.Button(basic_info_frame, text="SEARCH", bg="#ff0000", fg="#ffffff", font=("Arial", 10))
search_button.place(x=250, y=70)

tk.Label(basic_info_frame, text="Department:", bg="#ffffff").place(x=10, y=100)
department = tk.Entry(basic_info_frame, width=30)
department.place(x=150, y=100)


personal_info_frame = tk.Frame(root, bg="#ffffff", relief="solid", bd=1)
personal_info_frame.place(x=380, y=50, width=400, height=200)

tk.Label(personal_info_frame, text="Personal Information:", font=("Arial", 12, "bold"), bg="#ffffff").pack(anchor="w", padx=10, pady=5)

fields = ["Firstname", "Middle Name", "Surname", "Civil Status", "Qualified Dependents Status", "Paydate", "Employee Status", "Designation"]
for i, field in enumerate(fields):
    tk.Label(personal_info_frame, text=f"{field}:", bg="#ffffff").place(x=10, y=30 + (i * 20))
    tk.Entry(personal_info_frame, width=25).place(x=200, y=30 + (i * 20))


income_frame = tk.Frame(root, bg="#ffffff", relief="solid", bd=1)
income_frame.place(x=10, y=270, width=350, height=200)

tk.Label(income_frame, text="BASIC INCOME:", font=("Arial", 12, "bold"), bg="#ffffff").pack(anchor="w", padx=10, pady=5)
income_fields = ["Rate/Hour", "No. of Hours / Cut Off", "Income / Cut Off"]
for i, field in enumerate(income_fields):
    tk.Label(income_frame, text=f"{field}:", bg="#ffffff").place(x=10, y=40 + (i * 40))
    tk.Entry(income_frame, width=20).place(x=200, y=40 + (i * 40))


deductions_frame = tk.Frame(root, bg="#ffffff", relief="solid", bd=1)
deductions_frame.place(x=380, y=270, width=400, height=200)

tk.Label(deductions_frame, text="REGULAR DEDUCTIONS:", font=("Arial", 12, "bold"), bg="#ffffff").pack(anchor="w", padx=10, pady=5)
deduction_fields = ["SSS Contribution", "PhilHealth Contribution", "Pagibig Contribution", "Income Tax Contribution"]
for i, field in enumerate(deduction_fields):
    tk.Label(deductions_frame, text=f"{field}:", bg="#ffffff").place(x=10, y=40 + (i * 40))
    tk.Entry(deductions_frame, width=25).place(x=200, y=40 + (i * 40))


summary_frame = tk.Frame(root, bg="#ffffff", relief="solid", bd=1)
summary_frame.place(x=10, y=480, width=770, height=100)

tk.Label(summary_frame, text="SUMMARY INCOME:", font=("Arial", 12, "bold"), bg="#ffffff").pack(anchor="w", padx=10, pady=5)
tk.Label(summary_frame, text="GROSS INCOME:", bg="#ffffff").place(x=10, y=40)
tk.Entry(summary_frame, width=15).place(x=150, y=40)

tk.Label(summary_frame, text="NET INCOME:", bg="#ffffff").place(x=300, y=40)
tk.Entry(summary_frame, width=15).place(x=400, y=40)

# Action Buttons
tk.Button(root, text="GROSS INCOME", bg="#007bff", fg="white", width=12).place(x=10, y=590)
tk.Button(root, text="NET INCOME", bg="#28a745", fg="white", width=12).place(x=140, y=590)
tk.Button(root, text="SAVE", bg="#ffc107", fg="black", width=12).place(x=270, y=590)
tk.Button(root, text="UPDATE", bg="#17a2b8", fg="white", width=12).place(x=400, y=590)
tk.Button(root, text="NEW", bg="#6c757d", fg="white", width=12).place(x=530, y=590)


root.mainloop()
