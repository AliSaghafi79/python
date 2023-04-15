# sum matrix :
n = int(input('Enter the number of rows and columns  :  ' ))
def sum_matrix(rows,cols):
    mat=[]
    for i in range(rows):
        temp=[]
        for j in range(cols):
            temp.append(int(input("row ({}) , column ({})  :  ".format(i,j))))
        mat.append(temp)
    return mat
mat1=sum_matrix(n,n)
mat2=sum_matrix(n,n)
mat3=[]
for i in range (len(mat1)):
    temp=[]
    for j in range(len(mat1[0])):
        temp.append(mat1[i][j]+mat2[i][j])
    mat3.append(temp)
print(" ")
print("Matrix 1 = ")
for row in mat1 :
    print(row)

print(" ")
print("Matrix 2 = ")
for row in mat2 :
    print(row)

print(" ")
print("Matrix 1  +  Matrix 2 = ")
for row in mat3 :
    print(row)



