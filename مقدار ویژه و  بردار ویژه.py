import numpy as np
n = int(input('Enter the number of rows and columns  :  ' ))

def V_Matrix(rows,cols):

    mat = []
    for i in range( rows ):
        temp = []
        for j in range( cols ):
            temp.append(int(input("row ({}) , column ({})  :  ".format(i,j)  )))
        mat.append(temp)
    return mat

matrix = V_Matrix(n,n)

print(" ")

print("Matrix ({}×{}) = ".format(n,n))

for row in matrix :
    print(row)

values , vectors = np.linalg.eig( matrix )

print(" ")

print("Values = ")
print(values)

print(" ")

print("Vectors = ")

print(vectors)