
width  = int(input("Width? "))
height = int(input("Height? "))
star = "*"
space = " "
line = star * width
print(line)
i = 1
while i <= (height - 2):
    print(f"{star}{space * (width-2)}{star}")
    i +=1
print(line)