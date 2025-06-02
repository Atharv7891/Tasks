import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

def translate_gui_logic():
    word = entry.get().strip().lower()
    if not word:
        messagebox.showinfo("Error", "Please enter a word.")
        return


    if word[0] in "aeiou":
        current_hour = datetime.now().hour
        if current_hour != 21:
            output.delete(1.0, tk.END)
            output.insert(tk.END, " This word starts with a vowel , Please provide another word.")
            return


    seq = eng_tok.texts_to_sequences([word])
    padded = pad_sequences(seq, maxlen=eng_max, padding='post')
    pred = model.predict(padded)[0]
    decoded = [np.argmax(p) for p in pred]
    translation = ' '.join(hin_index_word.get(i, '') for i in decoded if i != 0).strip()

    output.delete(1.0, tk.END)
    output.insert(tk.END, f"Hindi: {translation}")


app = tk.Tk()
app.title("English to Hindi Translator")


tk.Label(app, text="Enter English Word:").pack(pady=5)
entry = tk.Entry(app, width=40)
entry.pack(pady=5)

tk.Button(app, text="Translate", command=translate_gui_logic).pack(pady=5)

output = tk.Text(app, height=5, width=50)
output.pack(pady=5)


app.mainloop()
