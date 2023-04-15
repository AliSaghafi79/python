n = int(input('Enter the number of rows and columns :  ' ))
def Multiplication_matrix(rows,cols):

    mat=[]
    for i in range(rows):
        temp=[]
        for j in range(cols):
            temp.append(int(input("row ({}) , column ({})  :  ".format(i,j)  )))
        mat.append(temp)
    return mat
print(" ")
matrix1=Multiplication_matrix(n,n)
print(" ")
print('Enter the number of rows and columns of matrix2 :  ')
matrix2=Multiplication_matrix(n,n)
print(" ")
print("matrix 1 = ")
for row in matrix1 :
    print(row)
print(" ")
print("matrix 2 = ")
for row in matrix2 :
    print(row)
x = []
for i in range(len(matrix1)) :
    matrix=[]
    for j in range (len(matrix1)) :
        result = 0
        for r in range(len(matrix1)) :
            result += matrix1[i][r] * matrix2[r][j]
        matrix.append(result)
    x.append(matrix)
print(" ")
print("matrix 1 ×  matrix 2  = ")
for row in x :
    print(row)
