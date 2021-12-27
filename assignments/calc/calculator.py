from tkinter import *

bg_col = "#3399ff"
entry_font = ("ariel", 20, "bold")

btn_bg_col = "#80bfff"
btn_font = ("new times roman", 12)

expression = ""


def test():
    print("A button was clicked")


def press(n):
    global expression
    expression += str(n)
    equation.set(expression)


def equal():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ''


def clear():
    global expression
    expression = ''
    equation.set("0")


def backspace():
    global expression
    expression = expression.rstrip(expression[-1])
    equation.set(expression)


window = Tk()
window.geometry("350x500")
window.title("Tom's PyCal")
window.configure(bg=bg_col)
#window.iconbitmap("calculator_icon.ico")

expression_frame = Frame(window, bg=bg_col)
buttons_frame = Frame(window, bg=bg_col)
expression_frame.pack()
buttons_frame.pack()

equation = StringVar()
equation.set("0")
equation_field = Entry(
	expression_frame, textvariable=equation, font=entry_font, justify="right")
equation_field.pack(ipadx=10, ipady=10, pady=20)

btn_params = dict()
btn_params["width"] = 8
btn_params["height"] = 3
btn_params["relief"] = "ridge"
btn_params["bg"] = btn_bg_col
btn_params["font"] = btn_font
btn_params["borderwidth"] = 1

button1 = Button(buttons_frame, text="1", **
                 btn_params, command=lambda: press(1))
button2 = Button(buttons_frame, text="2", **
                 btn_params, command=lambda: press(2))
button3 = Button(buttons_frame, text="3", **
                 btn_params, command=lambda: press(3))
button_plus = Button(buttons_frame, text="+", **
                     btn_params, command=lambda: press("+"))
button4 = Button(buttons_frame, text="4", **
                 btn_params, command=lambda: press(4))
button5 = Button(buttons_frame, text="5", **
                 btn_params, command=lambda: press(5))
button6 = Button(buttons_frame, text="6", **
                 btn_params, command=lambda: press(6))
button_min = Button(buttons_frame, text="-", **btn_params,
                    command=lambda: press("-"))
button7 = Button(buttons_frame, text="7", **
                 btn_params, command=lambda: press(7))
button8 = Button(buttons_frame, text="8", **
                 btn_params, command=lambda: press(8))
button9 = Button(buttons_frame, text="9", **
                 btn_params, command=lambda: press(9))
button_x = Button(buttons_frame, text="*", **btn_params,
                  command=lambda: press("*"))
button0 = Button(buttons_frame, text="0", **
                 btn_params, command=lambda: press(0))
button_dec = Button(buttons_frame, text=".", **btn_params,
                    command=lambda: press("."))
button_clr = Button(buttons_frame, text="C", **btn_params, command=clear)
button_div = Button(buttons_frame, text="/", **btn_params,
                    command=lambda: press("/"))
button_eq = Button(buttons_frame, text="=", **btn_params, command=equal)
button_back = Button(buttons_frame, text="<<", **btn_params, command=backspace)

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
button_plus.grid(row=0, column=3)

button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
button_min.grid(row=1, column=3)

button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
button_x.grid(row=2, column=3)

button0.grid(row=3, column=0)
button_dec.grid(row=3, column=1)
button_clr.grid(row=3, column=2)
button_div.grid(row=3, column=3)

button_eq.grid(row=4, column=0, columnspan=3, sticky="nsew")
button_back.grid(row=4, column=3)

window.mainloop()
