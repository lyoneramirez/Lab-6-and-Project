import tkinter as tk
from tkinter import ttk

#main application window
root = tk.Tk()
root.title("Meralco Application Form")
root.geometry("700x600")
root.configure(bg="#ffffff")  # White background

# Header Section
tk.Label(root, text="ACCREDITED MERALCO CONTRACTORS (AMC)", font=("Arial", 14, "bold"), bg="#ffffff", fg="#ff8c00").pack(pady=10)
tk.Label(root, text="APPLICATION FORM", font=("Arial", 12), bg="#ffffff").pack()
tk.Label(root, text="Type of Accreditation:", font=("Arial", 10), bg="#ffffff").pack(anchor="w", padx=20, pady=5)

# Accreditation Options
frame_accreditation = tk.Frame(root, bg="#ffffff")
frame_accreditation.pack(anchor="w", padx=40)
tk.Checkbutton(frame_accreditation, text="Home and Microbiz (HMB)", bg="#ffffff", font=("Arial", 10)).pack(side="left")
tk.Checkbutton(frame_accreditation, text="Small and Medium Enterprise (SME)", bg="#ffffff", font=("Arial", 10)).pack(side="left")

# Applicant Information Section
tk.Label(root, text="APPLICANT INFORMATION", font=("Arial", 12, "bold"), bg="#ffffff", fg="#000000").pack(anchor="w", padx=20, pady=10)

fields_applicant = ["Business Name", "Office Address", "Landline No.", "Fax No.", "E-mail Address"]
for field in fields_applicant:
    tk.Label(root, text=f"{field}:", font=("Arial", 10), bg="#ffffff").pack(anchor="w", padx=40)
    tk.Entry(root, font=("Arial", 10), width=50).pack(anchor="w", padx=40, pady=5)

# Representative Information Section
tk.Label(root, text="REPRESENTATIVE INFORMATION", font=("Arial", 12, "bold"), bg="#ffffff", fg="#000000").pack(anchor="w", padx=20, pady=10)

fields_representative = ["Name-Position", "Landline or Mobile No.", "Fax No.", "E-mail Address"]
for field in fields_representative:
    tk.Label(root, text=f"{field}:", font=("Arial", 10), bg="#ffffff").pack(anchor="w", padx=40)
    tk.Entry(root, font=("Arial", 10), width=50).pack(anchor="w", padx=40, pady=5)

tk.Label(root, text="Type of Ownership:", font=("Arial", 10), bg="#ffffff").pack(anchor="w", padx=20, pady=5)
frame_ownership = tk.Frame(root, bg="#ffffff")
frame_ownership.pack(anchor="w", padx=40)
ownership_types = ["Single Proprietorship", "Partnership", "Corporation", "Cooperative"]
for type_ in ownership_types:
    tk.Checkbutton(frame_ownership, text=type_, bg="#ffffff", font=("Arial", 10)).pack(side="left", padx=5)

tk.Label(root, text="Affiliation (whenever applicable):", font=("Arial", 10), bg="#ffffff").pack(anchor="w", padx=20, pady=5)
frame_affiliation = tk.Frame(root, bg="#ffffff")
frame_affiliation.pack(anchor="w", padx=40)
affiliations = ["Institute of Integrated Electrical Engineers (IIEE)", "Society of Philippine Electrotechnical Constructors and Suppliers Inc. (SPECS)"]
for affiliation in affiliations:
    tk.Checkbutton(frame_affiliation, text=affiliation, bg="#ffffff", font=("Arial", 10)).pack(anchor="w")

tk.Label(root, text="I hereby declare that all information supplied in this application is true and correct to the best of my belief and knowledge.", font=("Arial", 10), bg="#ffffff", wraplength=650).pack(pady=10, padx=20)

# Submit Button
tk.Button(root, text="Submit", font=("Arial", 12, "bold"), bg="#ff8c00", fg="#ffffff", width=10).pack(pady=20)

# Run the application
root.mainloop()
