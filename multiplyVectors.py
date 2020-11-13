

# Given two lists of numbers of the same length, create a new list by multiplying the pairs of numbers in corresponding positions in the two lists. Example:

#  x [2, 3, 6] = [4, 12, 30]

list1 = [2, 4, 5]
list2 = [2, 3, 6]
result = []
for i in range(0,len(list1)):
    result.append(list1[i]*list2[i])
print(result)