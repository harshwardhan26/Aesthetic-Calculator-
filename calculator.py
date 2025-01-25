from tkinter import Tk, Entry, StringVar, Button

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("545x430")
        master.config(bg="gray")

        self.equation = StringVar()
        self.entry_value = ""
        Entry(master, width=36, font=('Arial Bold', 24), textvariable=self.equation,  bg="#ffffff",fg='black', justify='right').grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('CLC', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('/', 4, 2), ('+', 4, 3),
            ('(', 5, 0), (')', 5, 1), ('%', 5, 2), ('=', 5, 3)
        ]

        for (text, row, col) in buttons:
            Button(master, text=text, width=10, height=3, command=lambda t=text: self.show(t) if t != '=' and t != 'CLC' else (self.solve() if t == '=' else self.clear()), bg="#93e6b8").grid(row=row, column=col, padx=5, pady=5)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ""
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.equation.get().replace('x', '*'))
            self.equation.set(result)
        except Exception:
            self.equation.set("Error")

root = Tk()
calculator = Calculator(root)
root.mainloop()