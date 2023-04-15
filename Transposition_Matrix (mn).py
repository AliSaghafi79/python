# n در m   ترانهاده یک ماتریس
import numpy as np
n = int(input('Enter the number of rows  :  ' ))
m = int(input("Enter the number of columns  :  "))
def Transposition_Matrix(rows,cols):

    mat=[]
    for i in range(rows):
        temp=[]
        for j in range(cols):
            temp.append(int(input("row ({}) , column ({})  :  ".format(i,j)  )))
        mat.append(temp)
    return mat

matrix=np.array(Transposition_Matrix(n,m))
print(" ")
print("Matrix ({}×{})  = ".format(n,m))
for row in matrix :
    print(row)

print(" ")
print("Transposition_Matrix ({}×{})  = ".format(n,m))
print(matrix.T)