
import tkinter as tk
from tkinter import messagebox

def on_click(button_text):
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            messagebox.showerror("Erreur", "Calcul invalide")
            entry.delete(0, tk.END)
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

root = tk.Tk()
root.title("Calculatrice HTML/Python")
root.geometry("300x400")
root.configure(bg="#1a1a2e")

entry = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="flat", justify='right', bg="#0f3460", fg="#e94560")
entry.pack(pady=20, padx=10, fill="x")

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

frame = tk.Frame(root, bg="#1a1a2e")
frame.pack()

row, col = 0, 0
for btn in buttons:
    tk.Button(frame, text=btn, width=5, height=2, font=("Arial", 14),
              command=lambda b=btn: on_click(b), bg="#16213e", fg="white", relief="flat").grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
