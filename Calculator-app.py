import tkinter as tk

expression=""
display=""

# only pass strings to this
def press_button(out_button):
    global expression
    global display
    if(out_button!=""):
        expression = expression + str(out_button)
        display.set(str(expression))

def equal_press():
    global expression
    global display
    expression = str(eval(str(expression)))
    display.set(expression)

def clear():
    global expression
    global display
    expression=""
    display.set("")

if __name__ == "__main__": 
    # config
    root = tk.Tk()
    root.geometry("340x340")
    root.title("Calculator")
    root.configure(background="sky blue")
    display = tk.StringVar()
    expression_field = tk.Entry(root, textvariable=display,background="sky blue", font=("Arial",20,'bold'))
    expression_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    button_padx=5
    button_pady=5

    button_clear = tk.Button(root, text="C",command=lambda: clear(), height=2, width=7)
    button_clear.grid(row=1, column=0, padx=button_padx, pady=button_pady)

    button_div = tk.Button(root, text="/",command=lambda: press_button("/"), height=2, width=7)
    button_div.grid(row=1, column=1, padx=button_padx, pady=button_pady)

    button_mult = tk.Button(root, text="*",command=lambda: press_button("*"), height=2, width=7)
    button_mult.grid(row=1, column=2, padx=button_padx, pady=button_pady)

    button_substr = tk.Button(root, text="-",command=lambda: press_button("-"), height=2, width=7)
    button_substr.grid(row=1, column=3, padx=button_padx, pady=button_pady)

    button7 = tk.Button(root, text="7", command=lambda: press_button("7"), height=2, width=7)
    button7.grid(row=2, column=0, padx=button_padx, pady=button_pady)

    button8 = tk.Button(root, text="8", command=lambda: press_button("8"), height=2, width=7)
    button8.grid(row=2, column=1, padx=button_padx, pady=button_pady)

    button9 = tk.Button(root, text="9", command=lambda: press_button("9"), height=2, width=7)
    button9.grid(row=2, column=2, padx=button_padx, pady=button_pady)

    button_plus = tk.Button(root, text="+", command=lambda: press_button("+"), height=6, width=7)
    button_plus.grid(row=2, column=3, padx=button_padx, pady=button_pady, rowspan=2)

    button4 = tk.Button(root, text="4", command=lambda: press_button("4"), height=2, width=7)
    button4.grid(row=3, column=0, padx=button_padx, pady=button_pady)

    button5 = tk.Button(root, text="5", command=lambda: press_button("5"), height=2, width=7)
    button5.grid(row=3, column=1, padx=button_padx, pady=button_pady)

    button6 = tk.Button(root, text="6", command=lambda: press_button("6"), height=2, width=7)
    button6.grid(row=3, column=2, padx=button_padx, pady=button_pady)

    button1 = tk.Button(root, text="1", command=lambda: press_button("1"), height=2, width=7)
    button1.grid(row=4, column=0, padx=button_padx, pady=button_pady)

    button2 = tk.Button(root, text="2", command=lambda: press_button("2"), height=2, width=7)
    button2.grid(row=4, column=1, padx=button_padx, pady=button_pady)

    button3 = tk.Button(root, text="3", command=lambda: press_button("3"), height=2, width=7)
    button3.grid(row=4, column=2, padx=button_padx, pady=button_pady)

    button_equal = tk.Button(root, text="=", command=lambda: equal_press(), height=6, width=7)
    button_equal.grid(row=4, column=3, padx=button_padx, pady=button_pady, rowspan=2)

    button0 = tk.Button(root, text="0", command=lambda: press_button("0"), height=2, width=16)
    button0.grid(row=5, column=0, columnspan=2, padx=button_padx, pady=button_pady)

    button_dot = tk.Button(root, text=".", command=lambda: press_button("."), height=2, width=7)
    button_dot.grid(row=5, column=2, padx=button_padx, pady=button_pady)

    root.mainloop()