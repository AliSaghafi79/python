# n در n   ترانهاده یک ماتریس

x = int(input('Enter the number of rows and columns  :  ' ))
def Transposition_Matrix(rows,cols):

    mat=[]
    for i in range(rows):
        temp=[]
        for j in range(cols):
            temp.append(int(input("row ({}) , column ({})  :  ".format(i,j)  )))
        mat.append(temp)
    return mat

matrix=Transposition_Matrix(x,x)
print(" ")
print("Matrix ({}×{})  = ".format(x,x))
for row in matrix :
    print(row)

for k in range(len(matrix)) :
    for s in range (k) :
        matrix [s] [k] , matrix [k] [s] = matrix [k] [s] ,matrix [s] [k]
print(" ")
print("Transposition_Matrix ({}×{})  = ".format(x,x))
for row in matrix :
    print(row)
