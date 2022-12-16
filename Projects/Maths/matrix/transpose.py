r = int(input("Enter rows : "))
c = int(input("Enter columns : "))

mat = []
for i in range(r):
    row = []
    for j in range(c):
        print(f"Enter element {i+1}{j+1} : ")
        row.append(int(input()))
    mat.append(row)

print("Your matrix")
print(mat)

mat_t = []
for i in range(c):
    row = []
    for j in range(r):
        row.append(0)
    mat_t.append(row)
    
for i in range(r):
    row = []
    for j in range(c):
        mat_t[j][i] = mat[i][j]
        
print(mat_t)

# transpose
print('Transpose matrix')

        
