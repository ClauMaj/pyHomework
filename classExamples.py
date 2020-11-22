
# # 1. Student campus
# class Student: # main class
#     def __init__(self, firstName, lastName, campus):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.campus = campus
#     def printStudent(self):
#         print(f"{self.firstName} {self.lastName} campus: {self.campus}")

# class Campus:   # management class
#     def __init__(self):
#         self.students = []
#     def addStudent(self, firstName, lastName, campus):
#         student = Student(firstName, lastName, campus)
#         self.students.append(student)
#     def showCurrentStudents(self):
#         for studentObj in self.students:
#             print(f'{studentObj.firstName} {studentObj.lastName} {studentObj.campus}')

# dc = Campus() # management var
# dc.addStudent('Kanny', 'Mohommad', 'Houston') # add objects through management class
# dc.addStudent('Matthew', 'Chun', 'Seattle')
# dc.addStudent('Kim', 'Long', 'Atlanta')
# dc.addStudent('Joe', 'Stocks', 'Houston')
# dc.showCurrentStudents()  # show all students through management class

# 2. bank

class AccountHolder:
    def __init__(self, fName, accountType, status, balance):
        self.fName = fName
        self.accountType = accountType
        self.status = status
        self.balance = balance

class Bank:
    def __init__(self, name, address):
        self.name = name 
        self.address = address 
        self.accounts = []
    def open_new_account(self, fName, accountType, status, balance):
        newAccount = AccountHolder(fName, accountType, status, balance)
        self.accounts.append(newAccount)
    def show_account_holder(self):
        for item in self.accounts:
            print(f'name: {item.fName} status: {item.status} balance: {item.balance}')
    def show_bank_balance(self):
        bankBalance = 0
        for item in self.accounts:
            bankBalance += item.balance
        print(f'The bank {self.name} balance is: {bankBalance}')

suntrust = Bank("blabla", "woof")
suntrust.open_new_account("Yada","Savings", "Active", 100)
suntrust.open_new_account("Pffff","Savings", "Active", 500)
suntrust.show_account_holder()
suntrust.show_bank_balance()

