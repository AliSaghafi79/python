# # دترمینان ماتریس های 3 در 3
# تابع ماتریس 3 در 3 ای را تعریف میکنیم که 2 مؤلفه ردیف و ستون میگیرند
def det_Matrix3(rows,cols):

    mat=[]
    for i in range(rows):
        temp=[]
        for j in range(cols):
            temp.append(int(input("row ({}) , column ({})  :  ".format(i,j)  )))
        mat.append(temp)
    return mat
# متغیر زیر را تعریف میکنیم و تابع بالا را درونش صدا میزنیم

matrix=det_Matrix3(3,3)
print(" ")
# ماتریس بوجود آمده را چاپ میکنیم

print("Matrix (3 × 3) = ")
for row in matrix :
    print(row)
#متغیر زیر را تعریف میکنیم و درونش فرمول دترمینان ماتریس های 3 در 3 را مینویسیم

det_Matrix = ((matrix[0][0] * matrix[1][1] * matrix[2][2]) + (matrix[0][1] * matrix[1][2] * matrix[2][0]) + (matrix[0][2] * matrix[1][0] * matrix[2][1])) - ((matrix[0][2] * matrix[1][1] * matrix[2][0]) + (matrix[0][0] * matrix[1][2] * matrix[2][1]) + (matrix[0][1] * matrix[1][0] * matrix[2][2]))

print(" ")
# دترمینان ماتریس بوجود آمده را چاپ میکنیم

print("det Matrix (3 × 3) = {}".format(det_Matrix))