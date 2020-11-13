
myList = [1,1, 2, 3, 4, 5, 3, 5]
deDub = []
for i in range(len(myList)):  # i is the index
    if myList[i] not in deDub:
        deDub.append(myList[i])
# for item not in myList
#     deDub.append(item)
print(deDub)

