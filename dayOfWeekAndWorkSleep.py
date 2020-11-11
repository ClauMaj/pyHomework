# week 1 Tuesday Homework

# Ex. 4
day = int(input('\nDay (0-6)? '))
if day == 0:
    print('Sunday')
elif day == 1:
    print('Monday')
elif day == 2:
    print('Tuesday')
elif day == 3:
    print('Wednesday')
elif day == 4:
    print('Thursday')
elif day == 5:
    print('Friday')
elif day == 6:
    print('Saturday')
else:
    print('The number mut be between 0-6')
    

    # Ex. 5
if (day == 1) or (day == 2) or (day == 3) or (day == 4) or (day == 5):
    print('Go to work!')
else:
    print('Sleep in!')