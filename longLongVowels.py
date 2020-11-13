
test_string = input('Enter a word: ')
vowels = ['a','e','i','o','u']
new_string = ''
for i in range(len(test_string)):
    if i != 0 and test_string[i] == test_string[i-1] and test_string[i].lower() in vowels:
        new_string += test_string[i] * 3
    new_string += test_string[i]
print(new_string)

# dblvwl = input("Give me a word to double its long vowels: ")
# result = ""
# list = [v,t ,f ,f ]
# for i in range(0, len(dblvwl) - 1):
#     if dblvwl[i] == dblvwl[i+1] and dblvwl[i] in list :
#         result = dblvwl[0:i] + dblvwl[i]*3 + dblvwl[i:]
#         break
# print(result)