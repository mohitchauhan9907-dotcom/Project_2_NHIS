import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("330x480")

entry = tk.Entry(root, font=("Arial", 24 ,"bold"), borderwidth=16, justify="right")
entry.grid(row=0, column=0, columnspan=4,sticky="nsew",padx=15, pady=13, ipady=12 )


history_list = []
result_shown = False


def clear():
    entry.delete(0, tk.END)

def press(value):
    global result_shown

    if result_shown:
        entry.delete(0, tk.END)
        result_shown = False
    current = entry.get()

    if value == "(" and current and current[-1].isdigit():
        entry.insert(tk.END, "*(")
    else:
        entry.insert(tk.END, value)


def equal():
    global result_shown, history_list
    try:
        expression = entry.get()     
        result = eval(expression)
        history_list.append(f"{expression} = {result}")

        if len(history_list) > 5:
            history_list.pop(0)

        entry.delete(0, tk.END)
        entry.insert(0, result)
        result_shown = True
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        result_shown = True

def history():
    global history_list, result_shown
    if history_list:
        entry.delete(0, tk.END)
 
        for h in history_list:
            entry.insert(tk.END, h + " || ")
        result_shown = True

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

for i in range(4):
    root.grid_columnconfigure(i, weight=1, uniform="equal")    


BTN_BOLD =("Segoe UI", 11, "bold",)


btn_frame = tk.Frame(root)
btn_frame.grid(row=1,column=0,columnspan=4)    


tk.Button(btn_frame, text="🕘", width=7, height=2,fg="brown",font=BTN_BOLD,command=history).grid(row=1, column=0)
tk.Button(btn_frame, text="⌫", width=7, height=2,fg="brown",font=BTN_BOLD, command=backspace).grid(row=1, column=2)
tk.Button(btn_frame, text="AC", width=7, height=2,fg="brown",font=BTN_BOLD, command=clear).grid(row=1, column=1)
tk.Button(btn_frame, text="%", width=7, height=2, fg="brown",font=BTN_BOLD,command=lambda: press("/100")).grid(row=1, column=3)

tk.Button(btn_frame, text="1", width=7, height=2, font=BTN_BOLD,command=lambda: press("1")).grid(row=4, column=0,padx=2, pady=2)
tk.Button(btn_frame, text="2", width=7, height=2, font=BTN_BOLD,command=lambda: press("2")).grid(row=4, column=1,padx=2, pady=2)
tk.Button(btn_frame, text="3", width=7, height=2, font=BTN_BOLD,command=lambda: press("3")).grid(row=4, column=2,padx=2, pady=2)
tk.Button(btn_frame, text="-", width=7, height=2,fg="brown",font=BTN_BOLD, command=lambda: press("-")).grid(row=4, column=3,padx=2, pady=2)

tk.Button(btn_frame, text="7", width=7, height=2,font=BTN_BOLD, command=lambda: press("7")).grid(row=2, column=0,padx=2, pady=2)
tk.Button(btn_frame, text="8", width=7, height=2,font=BTN_BOLD, command=lambda: press("8")).grid(row=2, column=1,padx=2, pady=2)
tk.Button(btn_frame, text="9", width=7, height=2,font=BTN_BOLD, command=lambda: press("9")).grid(row=2, column=2 ,padx=2, pady=2)
tk.Button(btn_frame, text="/", width=7, height=2, fg="brown",font=BTN_BOLD,command=lambda: press("/")).grid(row=2, column=3 ,padx=2, pady=2)

tk.Button(btn_frame, text="4", width=7, height=2,font=BTN_BOLD, command=lambda: press("4")).grid(row=3, column=0,padx=2, pady=2)
tk.Button(btn_frame, text="5", width=7, height=2,font=BTN_BOLD, command=lambda: press("5")).grid(row=3, column=1,padx=2, pady=2)
tk.Button(btn_frame, text="6", width=7, height=2,font=BTN_BOLD, command=lambda: press("6")).grid(row=3, column=2,padx=2, pady=2)
tk.Button(btn_frame, text="*", width=7, height=2,font=BTN_BOLD, fg="brown", command=lambda: press("*")).grid(row=3, column=3,padx=2, pady=2)

tk.Button(btn_frame, text="0", width=7, height=2,font=BTN_BOLD,command=lambda: press("0")).grid(row=5, column=0,padx=2, pady=2)
tk.Button(btn_frame, text="(", width=7, height=2,font=BTN_BOLD, command=lambda: press("(")).grid(row=5, column=1,padx=2, pady=2)
tk.Button(btn_frame, text=")", width=7, height=2,font=BTN_BOLD, command=lambda: press(")")).grid(row=5, column=2,padx=2, pady=2)

tk.Button(btn_frame, text="=", width=7, height=5,  fg="#FFFFFF",bg="#FC8F64",font=BTN_BOLD,command=equal).grid(row=5, column=3,rowspan=4, padx=2, pady=2)
tk.Button(btn_frame, text="00", width=7, height=2, font=BTN_BOLD,command=lambda: press("00")).grid(row=6, column=0,padx=2, pady=2)
tk.Button(btn_frame, text="+", width=7, height=2,fg="brown",font=BTN_BOLD, command=lambda: press("+")).grid(row=6, column=2,padx=2, pady=2)
tk.Button(btn_frame, text=".", width=7, height=2,font=BTN_BOLD,command=lambda: press(".")).grid(row=6, column=1,padx=2, pady=2)


root.mainloop()