from element_row import ElementRow
from table import TableSimplex
from numpy import array

table_dict = {
    "num_ecuaciones": 5,
    "num_variables" : 2,
    "positions" : 0,
    "table": array([
        [[0,-3],[0,-2], [0,0], [0,0], [0,0], [0,0], [0,0]],
        [[0,1], [0,2], [0,1], [0,0], [0,0], [0,0], [0,6]],
        [[0,2], [0,1], [0,0], [0,1], [0,0], [0,0], [0,8]],
        [[0,-1] ,[0,1] ,[0,0], [0,0], [0,1], [0,0], [0,1]],
        [[0,0], [0,1], [0,0], [0,0], [0,0], [0,1], [0,2]]
    ])
}

table = TableSimplex(table_dict["num_ecuaciones"],table_dict["num_variables"],table_dict["positions"])

table.initialize_table(table_dict["table"])

a = table.table[0].multiplyrow_bynumber(2)
print(a)
print(table)


