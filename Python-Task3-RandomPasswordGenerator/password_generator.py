import tkinter as tk
from tkinter import messagebox
import random
import string

# Generate Password
def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4.")
            return

        characters = ""

        if upper_var.get():
            characters += string.ascii_uppercase

        if lower_var.get():
            characters += string.ascii_lowercase

        if number_var.get():
            characters += string.digits

        if symbol_var.get():
            characters += string.punctuation

        if characters == "":
            messagebox.showerror("Error", "Select at least one option.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid password length.")

# Copy Password
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Clear Fields
def clear_fields():
    length_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Main Window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("450x450")
root.resizable(False, False)

title = tk.Label(root, text="Random Password Generator",
                 font=("Arial", 18, "bold"), fg="darkblue")
title.pack(pady=15)

tk.Label(root, text="Password Length", font=("Arial", 12)).pack()

length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.pack(pady=5)

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase Letters",
               variable=upper_var).pack(anchor="w", padx=80)

tk.Checkbutton(root, text="Include Lowercase Letters",
               variable=lower_var).pack(anchor="w", padx=80)

tk.Checkbutton(root, text="Include Numbers",
               variable=number_var).pack(anchor="w", padx=80)

tk.Checkbutton(root, text="Include Symbols",
               variable=symbol_var).pack(anchor="w", padx=80)

tk.Button(root,
          text="Generate Password",
          bg="green",
          fg="white",
          font=("Arial", 12),
          command=generate_password).pack(pady=15)

password_entry = tk.Entry(root, width=35, font=("Arial", 12))
password_entry.pack()

tk.Button(root,
          text="Copy Password",
          bg="blue",
          fg="white",
          font=("Arial", 12),
          command=copy_password).pack(pady=10)

tk.Button(root,
          text="Clear",
          bg="gray",
          fg="white",
          font=("Arial", 12),
          command=clear_fields).pack()

root.mainloop()