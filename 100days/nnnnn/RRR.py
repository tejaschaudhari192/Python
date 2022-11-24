  for r in range(r1):
        u=[]
        for s in range(c2):
            u.append(int(0))
        result.append(u)

    for r in range(r1): 
        for s in range(c2): 
            result[r][s]

    print("\nResult is: \n")


    # iterate through rows of r1
    for x in range(len(mat1)):
       # iterate through columns of c2
       for y in range(len(mat2[0])):
           # iterate through rows of r2
           for z in range(len(mat2)):
                result[x][y] += mat1[x][z] * mat2[z][y]
    for r in result:
        print(r)