import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.calc_value = 0.0
        self.div_trigger = False
        self.mult_trigger = False
        self.add_trigger = False
        self.sub_trigger = False

        # StringVar for entry
        self.entry_value = tk.StringVar(root, value="")

        # Window setup
        root.title("Calculator")
        root.geometry("500x250")
        root.resizable(width=False, height=False)

        style = ttk.Style()
        style.configure("TButton", font="serif 15", padding=10)
        style.configure("TEntry", font="serif 18", padding=10)

        # Entry widget
        self.number_entry = ttk.Entry(root, textvariable=self.entry_value, width=50)
        self.number_entry.grid(row=0, columnspan=4)

        # Row 1
        ttk.Button(root, text="7", command=lambda: self.button_press('7')).grid(row=1, column=0)
        ttk.Button(root, text="8", command=lambda: self.button_press('8')).grid(row=1, column=1)
        ttk.Button(root, text="9", command=lambda: self.button_press('9')).grid(row=1, column=2)
        ttk.Button(root, text="/", command=lambda: self.math_button_press('/')).grid(row=1, column=3)

        # Row 2
        ttk.Button(root, text="4", command=lambda: self.button_press('4')).grid(row=2, column=0)
        ttk.Button(root, text="5", command=lambda: self.button_press('5')).grid(row=2, column=1)
        ttk.Button(root, text="6", command=lambda: self.button_press('6')).grid(row=2, column=2)
        ttk.Button(root, text="*", command=lambda: self.math_button_press('*')).grid(row=2, column=3)

        # Row 3
        ttk.Button(root, text="1", command=lambda: self.button_press('1')).grid(row=3, column=0)
        ttk.Button(root, text="2", command=lambda: self.button_press('2')).grid(row=3, column=1)
        ttk.Button(root, text="3", command=lambda: self.button_press('3')).grid(row=3, column=2)
        ttk.Button(root, text="+", command=lambda: self.math_button_press('+')).grid(row=3, column=3)

        # Row 4
        ttk.Button(root, text="AC", command=self.clear_entry).grid(row=4, column=0)
        ttk.Button(root, text="0", command=lambda: self.button_press('0')).grid(row=4, column=1)
        ttk.Button(root, text="=", command=self.equal_button_press).grid(row=4, column=2)
        ttk.Button(root, text="-", command=lambda: self.math_button_press('-')).grid(row=4, column=3)

    def button_press(self, value):
        entry_val = self.number_entry.get()
        entry_val += value
        self.number_entry.delete(0, "end")
        self.number_entry.insert(0, entry_val)

    def clear_entry(self):
        self.number_entry.delete(0, "end")

    def is_float(self, str_val):
        try:
            float(str_val)
            return True
        except ValueError:
            return False

    def math_button_press(self, value):
        if self.is_float(self.number_entry.get()):
            self.add_trigger = self.sub_trigger = self.div_trigger = self.mult_trigger = False
            self.calc_value = float(self.entry_value.get())

            if value == "+":
                self.add_trigger = True
            elif value == "-":
                self.sub_trigger = True
            elif value == "/":
                self.div_trigger = True
            else:
                self.mult_trigger = True

            self.number_entry.delete(0, "end")

    def equal_button_press(self):
        if self.add_trigger or self.sub_trigger or self.div_trigger or self.mult_trigger:
            current_val = float(self.entry_value.get())
            if self.add_trigger:
                solution = self.calc_value + current_val
            elif self.sub_trigger:
                solution = self.calc_value - current_val
            elif self.div_trigger:
                solution = self.calc_value / current_val
            else:
                solution = self.calc_value * current_val

            self.number_entry.delete(0, "end")
            self.number_entry.insert(0, solution)


# Run program
if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
