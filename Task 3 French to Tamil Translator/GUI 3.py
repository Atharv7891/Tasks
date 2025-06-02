import tkinter as tk
from tkinter import messagebox

def translate_fra_gui():
    word = entry.get().strip()
    if len(word) != 5:
        messagebox.showinfo("Invalid Input", "Only the five letter words are allowed.")
        return
    translation = translate_fra_to_tam(word)
    output.delete(1.0, tk.END)
    output.insert(tk.END, f"Tamil: {translation}")

app = tk.Tk()
app.title("French to Tamil (5-letter only)")

tk.Label(app, text="Please Enter French Word:").pack()
entry = tk.Entry(app, width=40)
entry.pack()

tk.Button(app, text="Translate", command=translate_fra_gui).pack()

output = tk.Text(app, height=3, width=50)
output.pack()

app.mainloop()
