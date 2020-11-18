


# save
# data = {'name': 'Paul'}
# with open('data.pickle', 'wb') as fh:
#   pickle.dump(data, fh)

# load
# with open('data.pickle', 'rb') as fh:
#   data = pickle.load(fh)
#   print(data

# Electronic Phone Book
# =====================
# 1. Look up an entry
# 2. Set an entry
# 3. Delete an entry
# 4. List all entries
# 5. Quit

# What do you want to do (1-5)?
import pickle
import os.path

if os.path.isfile('phonebook.pickle'):
    with open('phonebook.pickle', 'rb') as fh:
        phonebook = pickle.load(fh)
else:
    phonebook = {}

def menu():
    print("""\nElectronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit""")
    return input("What do you want to do (1-5)? ")
    
def pick1():
    name1 = input("Who's phone number are you looking for? ")
    if name1 in phonebook:
        print(f"\n{name1}'s phone number is: {phonebook[name1]}")
    else:
        print(f"\nCould not find {name1}'s phone number.'")

def pick2():
    name2 = input("Name: ")
    phone2 = input("Phone number: ")
    phonebook[name2] = phone2
    print(f'Entry stored for {name2}.')

def pick3():
    name3 = input("Name: ")
    del phonebook[name3]
    print(f"Deleted entry for {name3}")

def pick4():
    count = 1
    for key, value in phonebook.items():
        if count == 1:
            print(f"\n{count}. Found entry for {key}: {value}")
        else:
            print(f"{count}. Found entry for {key}: {value}")
        count += 1

start = menu()

while start != '5':
    if start == '1':
        pick1()
        start = menu()
    elif start == '2':
        pick2()
        start = menu()
    elif start == '3':
        pick3()
        start = menu()
    elif start == '4':
        pick4()
        start = menu()
    else:
        print("\nWrong input, try again!")
        start = menu()


print(phonebook.items())

with open('phonebook.pickle', 'wb') as fh:
    pickle.dump(phonebook, fh)