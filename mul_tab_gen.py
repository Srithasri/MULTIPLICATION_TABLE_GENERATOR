import tkinter as tk
from tkinter import messagebox

def generate_table():
    try:
        num = int(entry.get())
        result_text.delete(1.0, tk.END)
        table = ""
        for i in range(1, 21):
            table += f"{i} x {num} = {num * i}\n"
        result_text.insert(tk.END, table)  
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")

root = tk.Tk()
root.title("Multiplication Table Generator")

label = tk.Label(root, text="Enter an integer:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Table", command=generate_table)
generate_button.pack(pady=10)

result_text = tk.Text(root, height=20, width=30)
result_text.pack(pady=10)

root.mainloop()
