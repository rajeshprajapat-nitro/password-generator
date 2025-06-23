import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())

        if length < 3:
            messagebox.showwarning("Invalid", "Password length should be at least 3!")
            return

        use_upper = var_upper.get()
        use_lower = var_lower.get()
        use_digits = var_digits.get()
        use_special = var_special.get()

        characters = ''
        if use_upper:
            characters += string.ascii_uppercase
        if use_lower:
            characters += string.ascii_lowercase
        if use_digits:
            characters += string.digits
        if use_special:
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Select at least one character set!")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")


# Create GUI window
root = tk.Tk()
root.title("Password Generator by Rajesh")
root.geometry("500x330")
root.config(bg="lightblue")
root.resizable(False,False)

# Widgets
rajesh=tk.Label(root,text="develop by Rajesh",font="(Arial,12)",bg="lightblue").pack(pady=5)
rajesh_lable=tk.Label(root, text="Password Length:", font=("Arial", 12), bg="lightblue").pack(pady=10)
length_entry = tk.Entry(root, font=("Arial", 12), width=10)
length_entry.pack()


# Checkboxes
var_upper = tk.BooleanVar()
var_lower = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_special = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase", variable=var_upper, font=("Arial", 10), bg="lightblue").pack()
tk.Checkbutton(root, text="Include Lowercase", variable=var_lower, font=("Arial", 10), bg="lightblue").pack()
tk.Checkbutton(root, text="Include Numbers", variable=var_digits, font=("Arial", 10), bg="lightblue").pack()
tk.Checkbutton(root, text="Include Special Characters", variable=var_special, font=("Arial", 10), bg="lightblue").pack()

# Generate button
tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12), bg="darkblue", fg="white").pack(pady=10)

# Result display
result_entry = tk.Entry(root, font=("Arial", 12), width=50,justify="center" )
result_entry.pack(pady=5,)

# Run GUI loop
root.mainloop()
