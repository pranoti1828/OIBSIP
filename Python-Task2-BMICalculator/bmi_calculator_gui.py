import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Invalid Input", "Weight and Height must be greater than 0.")
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
            color = "blue"
        elif bmi < 25:
            category = "Normal Weight"
            color = "green"
        elif bmi < 30:
            category = "Overweight"
            color = "orange"
        else:
            category = "Obese"
            color = "red"

        result_label.config(
            text=f"BMI : {bmi:.2f}\nCategory : {category}",
            fg=color
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")


# Clear Button
def clear_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")


# Main Window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x400")
root.resizable(False, False)

title = tk.Label(
    root,
    text="BMI CALCULATOR",
    font=("Arial", 18, "bold"),
    fg="darkblue"
)
title.pack(pady=15)

tk.Label(root, text="Enter Weight (kg)", font=("Arial", 12)).pack()

weight_entry = tk.Entry(root, font=("Arial", 12))
weight_entry.pack(pady=5)

tk.Label(root, text="Enter Height (m)", font=("Arial", 12)).pack()

height_entry = tk.Entry(root, font=("Arial", 12))
height_entry.pack(pady=5)

calculate_btn = tk.Button(
    root,
    text="Calculate BMI",
    font=("Arial", 12),
    bg="green",
    fg="white",
    command=calculate_bmi
)
calculate_btn.pack(pady=15)

clear_btn = tk.Button(
    root,
    text="Clear",
    font=("Arial", 12),
    bg="gray",
    fg="white",
    command=clear_fields
)
clear_btn.pack()

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold")
)
result_label.pack(pady=20)

root.mainloop()