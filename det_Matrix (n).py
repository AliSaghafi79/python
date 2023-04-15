# det matrix n × n :

import numpy as np
from math import *
n = int(input('Enter the number of rows and columns  :  ' ))
def det_Matrix(rows,cols):

    mat=[]
    for i in range(rows):
        temp=[]
        for j in range(cols):
            temp.append(int(input("row ({}) , column ({})  :  ".format(i,j)  )))
        mat.append(temp)
    return mat

matrix=det_Matrix(n,n)
print(" ")
print("Matrix ({}×{}) = ".format(n,n))
for row in matrix :
    print(row)
x = np.linalg.det(matrix)
print(" ")
print("det Matrix ({}×{}) = {}".format(n,n,ceil(x)))