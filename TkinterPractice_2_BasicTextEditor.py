import tkinter as tk
from tkinter.filedialog import askopenfilename


def open_file():
    filepath = askopenfilename(
        filetypes = [("Text Files", "*.txt")]
    )

    if not filepath:
        return
    
    text_box.delete("1.0", tk.END)
    with open(filepath, "r", encoding = 'utf-8') as input_file:
        text = input_file.read()
        text_box.insert(tk.END, text)
    window.title(f"Basic Text Editior - {filepath}")

def save_file():
    filepath = askopenfilename(
        defaultextension = ".txt",
        filetypes = [("Words", "*.txt")]
    )
    if not filepath:
        return
    
    with open(filepath, 'w') as output_file:
        text = text_box.get("1.0", tk.END)
        output_file.write(text)

    window.title(f"Basic Text Editior - {filepath}")
window = tk.Tk()
window.title(f"Basic Text Editior")

window.columnconfigure(1, weight = 1, minsize = 800)
window.rowconfigure(0, weight = 1, minsize = 800)

text_box = tk.Text(master=window)
text_box.grid(column = 1,row = 0, sticky = "nsew")

btn_cont = tk.Frame(master = window, relief= tk.RAISED, bd = 2)
btn_cont.grid(column=0, row=0, sticky="ns")

open_btn = tk.Button(btn_cont, text = "Open", command = open_file)
open_btn.grid(row = 0, column = 0, padx=5,pady=5,sticky="ew")

save_btn = tk.Button(btn_cont, text = "Save as", command = save_file)
save_btn.grid(row = 1, column = 0, padx=5,sticky="ew")
              

window.mainloop()
