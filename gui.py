import tkinter as tk
from tkinter import messagebox
from database import insert_student, fetch_students

def add_student():
    name = name_entry.get()
    age = age_entry.get()
    grade = grade_entry.get()

    if not name or not age or not grade:
        messagebox.showwarning("Input Error", "All fields are required.")
        return

    insert_student(name, int(age), grade)
    messagebox.showinfo("Success", "Student added successfully.")
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)

def show_students():
    students = fetch_students()
    display.delete('1.0', tk.END)
    for s in students:
        display.insert(tk.END, f"ID: {s[0]}, Name: {s[1]}, Age: {s[2]}, Grade: {s[3]}\n")

root = tk.Tk()
root.title("Student Management System")

tk.Label(root, text="Name").grid(row=0, column=0)
tk.Label(root, text="Age").grid(row=1, column=0)
tk.Label(root, text="Grade").grid(row=2, column=0)

name_entry = tk.Entry(root)
age_entry = tk.Entry(root)
grade_entry = tk.Entry(root)

name_entry.grid(row=0, column=1)
age_entry.grid(row=1, column=1)
grade_entry.grid(row=2, column=1)

tk.Button(root, text="Add Student", command=add_student).grid(row=3, column=0, pady=10)
tk.Button(root, text="View Students", command=show_students).grid(row=3, column=1)

display = tk.Text(root, width=50, height=10)
display.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
