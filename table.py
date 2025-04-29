import numpy as np
from numpy import array

from element_row import ElementRow

class TableSimplex:
    def __init__(self , num_ecu, variables):
        self.table = np.zeros(num_ecu, dtype=ElementRow)
        self.num_variables = variables
        self.num_equations = num_ecu
        self.basic_variables = np.zeros(num_ecu , dtype="U10")
        self.variable = np.zeros(variables + num_ecu + 1, dtype= "U10")

    def __str__(self):
        leap = (self.num_equations + self.num_variables + 1) * 10
        table = "-" * leap
        table += "\n|   "
        for i in range(len(self.variable)):
            table +=   self.variable[i] + "   |    "
        table+= "\n"
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

        a = 1
        for i in range(self.num_variables + self.num_equations):
            if i == 0:
                self.variable[i] = "VB"
            elif i <= self.num_variables and self.num_variables >0:
                self.variable[i] = f"X{i}"
            else:
                self.variable[i] = f"H{a}"
                a += 1

            self.variable[len((self.variable)) - 1] = f"LD"


    def __output_variable__(self,position):
        values_ld = np.zeros(len(self.table), dtype=int)
        values_column = np.zeros(len(self.table), dtype= int)        
        values = np.zeros(len(self.table) - 1,dtype=int)


        for i in range(len(self.table)):
            values_ld[i] = self.table[i].row[-1][1]
            values_column[i] = self.table[i].row[position][1]

        for i in range(len(values_ld[1:])):
            if values_column[i + 1] > 0:
                values[i] = values_ld[i + 1] / values_column[i + 1]

        menor = values[values > 0]

        return  int(np.where(values == values[menor.argmin()])[0] + 1)

    def solve_max(self):
        return 0

    def solve_min(self):
        return 0
