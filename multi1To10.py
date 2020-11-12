
i = 1
j = 1
while i <= 10:
    if j == 1:
        print(f"Multiplication for {i}") 
    print (f"{i} X {j} = {i*j}")
    j += 1
    if j == 11:
        i += 1
        j = 1
