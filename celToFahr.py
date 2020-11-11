
# week 1 Tuesday Homework

# Ex. 6

temp = float(input('Temperature in C? '))
cel = temp * 9 / 5 + 32
if cel  != int(cel):
    print('Temperature in F is: {}'.format(cel))
else: 
    print('Temperature in F is: {}'.format(int(cel)))
