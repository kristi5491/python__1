import tkinter as tk

win = tk.Tk()
win.geometry(f"550x300+100+200")
win['bg'] = '#8062c4'
win.title('task 1')

number = 6
number2 = 8.8
number3 = True
text2 = "orange"

data_types = f"{number}, {type(number)} ,  {number2}, {type(number2)}, {number3}, {type(number3)}, {text2}, {type(text2)}"

text = tk.Label(win, text=data_types, font=('Arial', 15), fg="pink")
text.pack()


win.mainloop()