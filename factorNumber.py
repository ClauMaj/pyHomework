
number = int(input("Please enter a number to check its factors: "))
i = 1
while i <= number:
    if number % i == 0:
        print(i)
    i += 1