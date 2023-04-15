#  trace :
n = int(input('Enter the number of rows and columns  :  ' ))
def trace_Matrix(rows,cols):

    mat=[]
    for i in range(rows):
        temp=[]
        for j in range(cols):
            temp.append(int(input("row ({}) , column ({})  :  ".format(i,j)  )))
        mat.append(temp)
    return mat


matrix=trace_Matrix(n,n)
print(" ")
print("Matrix ({}×{}) = ".format(n,n))
for row in matrix :
    print(row)

for k in range(len(matrix)) :
    x = matrix[k][k]
    for s in range (k) :
        x += matrix[s][s]
print(" ")
print("trace Matrix ({}×{})  = {} ".format(n,n,x))

