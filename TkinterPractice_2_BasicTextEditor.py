import tkinter as tk
from tkinter.filedialog import askopenfilename


def open_file():
    filetypes = askopenfilename(filetypes = [("Text Files", "*.txt"), ("All Files", "*.")])

    if not filetypes:
        return

    text_box.delete("1.0", tk.END)
    with open()

window = tk.Tk()
window.title("Basic Text Editior")

window.columnconfigure(1, weight = 1, minsize = 800)
window.rowconfigure(0, weight = 1, minsize = 800)

text_box = tk.Text(master=window)
text_box.grid(column = 1,row = 0, sticky = "nsew")

btn_cont = tk.Frame(master = window, relief= tk.RAISED, bd = 2)
btn_cont.grid(column=0, row=0, sticky="ns")

open_btn = tk.Button(btn_cont, text = "Open")
open_btn.grid(row = 0, column = 0, padx=5,pady=5,sticky="ew")

save_btn = tk.Button(btn_cont, text = "Save as")
save_btn.grid(row = 1, column = 0, padx=5,sticky="ew")
              

window.mainloop()
