import tkinter as tk

expression=""
display=""

# only pass strings to this
def press_button(out_button):
    global expression
    global display
    if(out_button!=""):
        expression = expression + out_button
        display.set(str(expression))

def equal_press():
    global expression
    global display
    display = eval(str(expression))
        
def clear():
    global expression
    global display
    expression=""
    display.set("0")

if __name__ == "__main__": 
    # config
    root = tk.Tk()
    root.geometry("400x400")
    root.title("Calculator")
    root.configure(background="sky blue")
    display = tk.StringVar()
    expression_field = tk.Entry(root, textvariable=display,background="sky blue", font=("Arial",18,'bold'))
    expression_field.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    button_padx=5
    button_pady=5

    button_clear = tk.Button(root, text="",command=lambda: clear(), height=1, width=7)
    button_clear.grid(row=1, column=0, padx=button_padx, pady=button_pady)

    button_div = tk.Button(root, text="/",command=lambda: press_button("/"), height=1, width=7)
    button_div.grid(row=1, column=1, padx=button_padx, pady=button_pady)

    button_mult = tk.Button(root, text="*",command=lambda: press_button("*"), height=1, width=7)
    button_mult.grid(row=1, column=2, padx=button_padx, pady=button_pady)

    button_substr = tk.Button(root, text="-",command=lambda: press_button("-"), height=1, width=7)
    button_substr.grid(row=1, column=3, padx=button_padx, pady=button_pady)

    button7 = tk.Button(root, text="7", command=lambda: press_button("7"), height=1, width=7)
    button7.grid(row=2, column=0, padx=button_padx, pady=button_pady)

    button8 = tk.Button(root, text="8", command=lambda: press_button("8"), height=1, width=7)
    button8.grid(row=2, column=1, padx=button_padx, pady=button_pady)

    button9 = tk.Button(root, text="9", command=lambda: press_button("9"), height=1, width=7)
    button9.grid(row=2, column=2, padx=button_padx, pady=button_pady)

    button_plus = tk.Button(root, text="+", command=lambda: press_button("+"), height=7, width=1)
    button_plus.grid(row=2, column=3, padx=button_padx, pady=button_pady, rowspan=2)

    button4 = tk.Button(root, text="4", command=lambda: press_button("4"), height=1, width=7)
    button4.grid(row=3, column=0, padx=button_padx, pady=button_pady)

    button5 = tk.Button(root, text="5", command=lambda: press_button("5"), height=1, width=7)
    button5.grid(row=3, column=1, padx=button_padx, pady=button_pady)

    button6 = tk.Button(root, text="6", command=lambda: press_button("6"), height=1, width=7)
    button6.grid(row=3, column=2, padx=button_padx, pady=button_pady)

    root.mainloop()