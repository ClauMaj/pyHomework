
# week 1 Tuesday Homework

# Ex. 6

temp = float(input('Temperature in C? '))
cel = temp * 9 / 5 + 32
if cel  == int(cel):
    print(f'Temperature in F is: {cel}')
else: 
    print(f'Temperature in F is: {int(cel)}')
