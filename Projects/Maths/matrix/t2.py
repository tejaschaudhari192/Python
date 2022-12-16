from mybuild import MakeMatrix,PrintMatrix
r = int(input("Enter rows : "))
c = int(input("Enter colms : "))

mat = MakeMatrix(r,c)


mat.remove(mat[1][1])

for i in mat:
    print(i)