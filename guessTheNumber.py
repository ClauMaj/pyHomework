
import random
my_random_number = random.randint(1, 10)

# my_random_number = 5
count = 0
guess = 0
print("I am thinking of a number between 1 and 10.")
while count < 5 and guess != my_random_number:
    print(f"You have {5-count} guesses left.")
    guess = int(input("What's the number? "))
    if guess == my_random_number:
        print("Yes! You win!")
    elif guess < my_random_number:
        print(f"{guess} is to low.")
    else:
        print(f"{guess} is to high.")
    count += 1    
    if count == 5 and guess != my_random_number:
        print("You ran out of guesses!")
    if count == 5 or guess == my_random_number:
        again = input("Do you want to play again (Y or N)? ").upper()
        if again == "Y":
            my_random_number = random.randint(1, 10)
            count = 0
            guess = 0
            print("\nI am thinking of a number between 1 and 10.")
