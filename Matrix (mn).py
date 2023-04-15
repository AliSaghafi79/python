#    #    نمایش  ماتریس های m در n

n = int(input('Enter the number of rows  :  ' ))
m = int(input("Enter the number of columns  :  "))
def get_matrix(rows,cols):

    mat=[]
    for i in range(rows):
        temp=[]
        for j in range(cols):
            temp.append(int(input("row ({}) , column ({})  :  ".format(i,j)  )))
        mat.append(temp)
    return mat

matrix=get_matrix(n,m)

for row in matrix :
    print(row)
