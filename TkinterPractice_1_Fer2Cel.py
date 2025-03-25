import tkinter as tk

window = tk.Tk()
window.geometry("300x150")

window.columnconfigure(0 , weight = 1, minsize = 1)
window.columnconfigure(1 , weight = 2, minsize = 50)
window.rowconfigure([0,1], weight = 1, minsize = 1)

def convert():
    value = int(input_entry.get())
    c = (value - 32) * (5/9)
    f_label['text'] = str(f"{c:.2f}")


frame0 = tk.Frame(master = window, bg = "white" )
frame0.grid(row = 0, column = 0, sticky = "nsew")

input_entry = tk.Entry(master = frame0, bg = "white", font = ("Times New Roman",12))
input_entry.pack()


frame1 = tk.Frame(master = window, bg = "blue", )
frame1.grid(row = 1, column = 0, sticky = "nsew")

convert_button = tk.Button(master = frame1, font = ("Calibri", 20, "bold"), text = "Convert", bg = 'blue', command = convert)
convert_button.pack(expand = True, fill = "both")


frame2 = tk.Frame(master = window, bg = "yellow", )
frame2.grid(row=0, column = 1, rowspan = 2, sticky = "nsew")

f_label = tk.Label(master = frame2, font=("Arial", 20, "italic"), bg = 'yellow', text = "0")
f_label.pack(expand = True)

window.mainloop()
