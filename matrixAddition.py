


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

# # Matrix Addition 
# list1 = [[1,3,5,6], [2,4,4,3]]
# list2 = [[5,2,1,0], [1,0,3,5]]
# add_list = []
# for row in range(0, len(list1)):
#     temp = []
#     for column in range(0, len(list1[0])):
#         temp.append(list1[row][column] + list2[row][column])
#     add_list.append(temp)
# print(add_list)