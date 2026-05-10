import tkinter as tk
from tkinter import messagebox

def on_click(button_text):
    current_text = entry.get()
    
    if button_text == "=":
        try:
            # eval handles the math logic (e.g., "27+8+1")
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
            entry.delete(0, tk.END)
            
    elif button_text == "AC":
        entry.delete(0, tk.END)
        
    elif button_text == "⌫": # Backspace logic
        entry.delete(len(current_text)-1, tk.END)
        
    else:
        entry.insert(tk.END, button_text)

# 1. Setup the main window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("350x500")
root.configure(bg="#f0f0f0")

# 2. The Display Screen
entry = tk.Entry(root, font=("Arial", 30), borderwidth=0, relief="flat", justify="right", bg="#f0f0f0")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=20, pady=40)

# 3. Button Labels (Layout matching your image)
buttons = [
    'AC', '%', '⌫', '/',
    '7', '8', '9', '*',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '00', '0', '.', '='
]

# 4. Create and place buttons
row_val = 1
col_val = 0

for button in buttons:
    # Color logic for the "=" button and operators
    bg_color = "#ffffff"
    fg_color = "#000000"
    if button == "=":
        bg_color = "#ff9f0a" # Orange
        fg_color = "#ffffff"
    elif button in ['AC', '%', '⌫', '/', '*', '-', '+']:
        bg_color = "#e0e0e0"

    action = lambda x=button: on_click(x)
    
    tk.Button(root, text=button, width=5, height=2, font=("Arial", 14),
              bg=bg_color, fg=fg_color, relief="flat",
              command=action).grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Make the grid expand evenly
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
