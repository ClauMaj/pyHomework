


mat1 = [[1 , 2], [3 , 4]]
mat2 = [[5 , 6], [7 , 8]]
if (len(mat1) == len(mat2)) and (len(mat1[0]) == len(mat2[0])):
    result = mat1.copy()
    for i in range(0,len(mat1)):
        for j in range(0,len(mat1[i])):
                result[i][j] = (mat1[i][j]+mat2[i][j])
    print(result)
else:
    print("Matrices are not equal")

