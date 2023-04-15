# det matrix 2 :

# تابع ماتریس 2 در 2 ای را تعریف میکنیم که 2 مؤلفه ردیف و ستون میگیرند

def det_Matrix2(rows,cols):

    mat=[]

    for i in range(rows):

        temp=[]

        for j in range(cols):

            temp.append(int(input("row ({}) , column ({})  :  ".format(i,j)  )))

        mat.append(temp)

    return mat

# متغیر زیر را تعریف میکنیم و تابع بالا را درونش صدا میزنیم
matrix=det_Matrix2(2,2)

print(" ")

# ماتریس بوجود آمده را چاپ میکنیم
for row in matrix :
    print(row)

#متغیر زیر را تعریف میکنیم و درونش فرمول دترمینان ماتریس های 2 در 2 را مینویسیم
det_Matrix = (matrix[0][0] * matrix[1][1] ) - (matrix[0][1] * matrix[1][0])


print(" ")

# دترمینان ماتریس بوجود آمده را چاپ میکنیم
print("det_Matrix = {}".format(det_Matrix))



