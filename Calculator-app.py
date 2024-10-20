import tkinter as tk

# config
root = tk.Tk()
root.geometry("300x300")
root.title("Calculator")
root.configure(background="sky blue")

# print(dir(root))
equation = tk.StringVar()
expression_field = tk.Entry(root, textvariable=equation,background="sky blue", font=("Arial",18,'bold'))
expression_field.grid(columnspan=4, ipadx=70)
root.mainloop()