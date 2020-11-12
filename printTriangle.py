
width = int(input("Please enter an odd number: "))
s = " "
n = "*"
i = 1
while i <= width:
    sp = int((width - i) / 2)
    print(f"{s * sp}{n * i}{s * sp}")
    i += 2