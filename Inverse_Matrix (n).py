# Inverse_Matrix n × n :
import numpy as np
n = int(input('Enter the number of rows and columns :  ' ))
def Inverse_Matrix(rows,cols):

    mat=[]
    for i in range(rows):
        temp=[]
        for j in range(cols):
            temp.append(int(input("row ({}) , column ({})  :  ".format(i,j)  )))
        mat.append(temp)
    return mat

matrix=Inverse_Matrix(n,n)
print(" ")
print("Matrix ({}×{}) = ".format(n,n))
for row in matrix :
    print(row)
print(" ")
Inverse_Matrix = np.linalg.inv(matrix)
print("Inverse Matrix  = ")
print(Inverse_Matrix)