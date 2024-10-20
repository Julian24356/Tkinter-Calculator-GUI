import tkinter as tk

# config
root = tk.Tk()
root.geometry("400x400")
root.title("Calculator")
root.configure(background="sky blue")

# print(dir(root))
result = tk.Label(root, text="Test", font=("Arial",18), background="sky blue", justify="left") # add border=
result.pack(anchor="w") # add padding pady=10, padx=10,
root.mainloop()