
bill = float(input("Total bill amount? "))
serv = input("Level of service? ")

if serv == "good":
    n = 20
elif serv == "fair":
    n = 15
elif serv == "bad":
    n = 10
else:
    print("Good, Fair or Bad")

tip = bill*n/100
print(f"Tip amount: {tip}")
total = tip + bill
print(f"Total amount: {total}")

split = input('Would you like to divide the bill? (yes/no)')
if split == "yes": 
    people = int(input("How many people would you like to divide amongst? "))
    final = total / people
    print(f"Amount per person: {final}")