# وارون ماتریس 2 در 2

def Inverse_Matrix(rows,cols):

    mat=[]
    for i in range(rows):
        temp=[]
        for j in range(cols):
            temp.append(int(input("row ({}) , column ({})  :  ".format(i,j)  )))
        mat.append(temp)
    return mat

matrix=Inverse_Matrix(2,2)
print(" ")
print("Matrix ({}×{}) = ".format(2,2))
for row in matrix :
    print(row)
det_Matrix = (matrix[0][0] * matrix[1][1] ) - (matrix[0][1] * matrix[1][0])
Inverse_Matrix = ([matrix[1][1] / det_Matrix,-matrix[0][1]/ det_Matrix] , [-matrix[1][0]/ det_Matrix,matrix[0][0]/ det_Matrix])
print(" ")
print("Inverse_Matrix (2×2) = ")
for row in Inverse_Matrix:
    print(row)