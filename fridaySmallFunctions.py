# 1. Madlib function
# madlibName = input("name: ")
# madlibSubject = input("subject: ")
# def interpolate(a, b):
#     print(f"{a}'s favorite subject is {b}.'")
# interpolate(madlibName,madlibSubject)


# 2.  Celsius to Fahrenheit conversion
# cel = int(input('cel temp: '))
# def celToFar(temp):
#     return (temp * 9/5) + 32

# print(celToFar(cel))

# 3.  Fahrenheit to Celsius conversion
# fah = int(input('Fahr temp: '))
# def fahrToCel(temp):
#     return (temp - 32) * 5/9

# print(fahrToCel(fah))

# 4 . is_even function
# num = int(input('number: '))
# def isEven(a):
#     if a % 2 == 0:
#         return True
#     else:
#         return False
# print(f'Even {isEven(num)}')

# 5. is_odd function
# def isOdd(b):
#     return not isEven(b)
# print(f'Odd {isOdd(num)}')

# 6. only_evens function
# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def evenlist(evenlist):
#     c = []
#     for item in evenlist:
#         if isEven(item):
#             c.append(item)
#     return c
# print(evenlist(myList))

# 7. only_odds function
# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def oddlist(oddlist):
#     d = []
#     for item in oddlist:
#         if isOdd(item):
#             d.append(item)
#     return d
# print(oddlist(myList))

# 6. only_evens function with remove
# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def evenlist(evenlist):
#     for item in evenlist:
#         if isEven(item):
#             evenlist.remove(item)
# print(evenlist(myList))
# print(myList)