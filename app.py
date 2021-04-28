from tkinter import Tk, Entry, Button, Grid, END


class Calculator:
    def __init__(self, master):

        """
        DOCSTRING: initialization
        file changed
        
        """

        self.master = master

        master.title("Python Calculator")

        self.equation = Entry(master, width=40, borderwidth=5)

        self.equation.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_button()

    def create_button(self):

        """
        DOCSTRING: Method that creates the buttons
        INPUT: nothing
        OUTPUT: creates a button
        """

        b_0 = self.add_button(0)
        b_1 = self.add_button(1)
        b_2 = self.add_button(2)
        b_3 = self.add_button(3)
        b_4 = self.add_button(4)
        b_5 = self.add_button(5)
        b_6 = self.add_button(6)
        b_7 = self.add_button(7)
        b_8 = self.add_button(8)
        b_9 = self.add_button(9)
        b_add = self.add_button("+")
        b_sub = self.add_button("-")
        b_mult = self.add_button("*")
        b_div = self.add_button("/")
        b_clear = self.add_button("c")
        b_equal = self.add_button("=")
        b_sqrroot = self.add_button("√")
        b_modulo = self.add_button("%")
        b_sqr = self.add_button("**2")
        b_inverse = self.add_button("1/x")
        b_sign = self.add_button("±")
        b_decimal = self.add_button(".")
        b_clear = self.add_button("C")
        b_clearall = self.add_button("CE")
        b_del = self.add_button("X")

        row1 = [b_modulo, b_sqrroot, b_sqr, b_inverse]
        row2 = [b_clearall, b_clear, b_del, b_div]
        row3 = [b_7, b_8, b_9, b_mult]
        row4 = [b_4, b_5, b_6, b_sub]
        row5 = [b_1, b_2, b_3, b_add]
        row6 = [b_sign, b_0, b_decimal, b_equal]

        row_index = 1
        for row in [row1, row2, row3, row4, row5, row6]:
            column_index = 0
            for button in row:
                button.grid(row=row_index, column=column_index, columnspan=1)
                column_index += 1
            row_index += 1

    def add_button(self, value):

        """
        DOCSTRING: Method to process the creation of a button and make it clickable
        INPUT: value of the button (1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,=)
        OUTPUT: returns a designed button object
        """
        return Button(
            self.master,
            text=value,
            width=9,
            command=lambda: self.clickButton(str(value)),
        )

    def clickButton(self, value):

        """
        DOCSTRING: Method to program the actions that will happen in the calculator after a click of each button
        INPUT: value of the button (1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,=)
        OUTPUT: what action will be performed when a particular button is clicked
        """
        current_equation = str(self.equation.get())
        try:
            if value in ("C", "CE"):
                self.equation.delete(-1, END)

            elif value == "=":
                if "√" in current_equation:
                    answer = eval(current_equation[: len(current_equation) - 1] + "**(1/2)")
                elif "1/x" in current_equation:
                    answer = eval(current_equation[: len(current_equation) - 3] + "**(-1)")
                else:
                    answer = str(eval(current_equation))
                self.equation.delete(-1, END)
                self.equation.insert(0, answer)

            elif value == "X":
                self.equation.delete(0, END)
                self.equation.insert(-1, current_equation[:-1])

            elif value == "±":
                self.equation.delete(0, END)
                self.equation.insert(-1, str(int(current_equation) * (-1)))
            else:
                self.equation.delete(0, END)
                self.equation.insert(-1, current_equation + value)
        except:
            self.equation.delete(0, END)
            self.equation.insert(-1, "Syntax error")


if __name__ == "__main__":

    root = Tk()
    my_gui = Calculator(root)

    root.mainloop()
