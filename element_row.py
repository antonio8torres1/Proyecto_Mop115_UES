import numpy as np
from numpy import array

class ElementRow:
    def __init__(self,size: int) -> None:
        self.row = np.zeros((size, 2) , dtype="float")

    def __str__(self):
        return str(self.row.tolist())

    def __add__(self, other):
        new_row = ElementRow(len(self.row))
        new_row.row = self.row + other.row
        return new_row

    def __sub__(self,other):
        new_row = ElementRow(len(self.row))
        new_row.row = self.row - other.row
        return new_row

    def set_element(self,values):
        if values.ndim == 2:            
            self.row = values
            self.row = self.row.astype(float)
        else:
            raise Exception("Array no concuerda con tipo [0,0]")

    def dividerow_bynumber(self, number: float):
        self.row /= number


    def multiplyrow_bynumber(self, number:float):
        self.row *= number

    def basic_values(self):
        values_m = self.row[:,0]
        values = self.row[:,1]

        if np.count_nonzero(values_m) == 0:
            return int(np.where(values == values[values > 0])[0]) , int(values.argmin())
        else:
            return int(values_m.argmax()) , int(values_m.argmin())



