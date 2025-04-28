import numpy as np
from numpy import array

from element_row import ElementRow

class TableSimplex:
    def __init__(self , num_ecu, variables, pos):
        self.table = np.zeros(num_ecu, dtype=ElementRow)
        self.positions = pos
        self.num_variables = variables
        self.num_equations = num_ecu
        self.basic_variables = np.zeros(num_ecu , dtype="U10")

    def __str__(self):
        leap = (self.num_equations + self.num_variables + 1) * 10
        table = "-" * leap
        table += "\n|"
        for i in range(self.num_variables + 1):
            if i == 0:
                table += f"   VB" + "   | "
            else:
                table += f"   X{i}" + "   | "

        for i in range(len(self.table) - 1):
            table += f"   H{i + 1}" + "   | "

        table += "  LD    |" + "\n"
        table += "-" * leap + "\n"
        for i in range(len(self.table)):
            table += f"|   " + self.basic_variables[i] +"   |   "
            # table += "|  "
            for j in range(self.num_variables + self.num_equations):
                table += str(self.table[i].row[j][1])
                if self.table[i].row[j][1] >= 0:
                    table += "   |   "
                else: table += "  |   "

            table+= "\n"

        return table

    def initialize_table(self, table):
        for i in range(len(table)):
            element = ElementRow(len(table))
            element.set_element(table[i])
            self.table[i] = element

        for i in range(len(table)):
            if i == 0:
                self.basic_variables[i] = "Z "
            else:
                self.basic_variables[i] = f"H{i}"

    def solve(self):
        return 0


