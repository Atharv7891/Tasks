import tkinter as tk
from tkinter import messagebox

def translate_dual_gui():
    text = entry.get()
    if len(text.replace(" ", "")) < 10:
        messagebox.showinfo("Error", "Please upload again.")
        return
    fra_result = translate(text, model_fra, fra_tok, fra_max, fra_index_word)
    hin_result = translate(text, model_hin, hin_tok, hin_max, hin_index_word)
    output.delete(1.0, tk.END)
    output.insert(tk.END, f"French: {fra_result}\nHindi: {hin_result}")

app = tk.Tk()
app.title("Dual Translator (English to French & Hindi)")

tk.Label(app, text="Please Enter English Text:").pack()
entry = tk.Entry(app, width=50)
entry.pack()

tk.Button(app, text="Translate", command=translate_dual_gui).pack()

output = tk.Text(app, height=5, width=60)
output.pack()

app.mainloop()
