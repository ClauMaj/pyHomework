
bill = float(input("Total bill amount? "))
serv = input("Level of service? ").lower()

if serv == "good":
    n = 20
elif serv == "fair":
    n = 15
elif serv == "bad":
    n = 10
else:
    print("good, fair or bad")

tip = bill*n/100
print(f"Tip amount: {tip:.2f}")
total = tip + bill
print(f"Total amount: {total:.2f}")

split = input('Would you like to divide the bill? (y/n)').lower()
if split == "y": 
    people = int(input("How many people would you like to divide amongst? "))
    final = total / people
    print(f"Amount per person: {final}")