# bank acc == owner, acc no, balance, history
from datetime import date, datetime
from time import strptime


class Client:
    def __init__(self, names:str, kra_pin:str, dob:str, gender:str, email:str):
        self.names = names
        self.kra_pin = kra_pin
        self.dob = dob
        self.gender = gender
        self.email = email

    def print_details(self):
        print(self.names)
        print(self.kra_pin)
        print(self.dob)
        print(self.gender)
        print(self.email)

    def calc_age(self):
        today = date.today()
        birth_date = datetime.strptime(self.dob, "%Y-%m-%d")
        age = today.year - birth_date.year
        return age


class BankAccount:
    def __init__(self, owner:Client, acc_no:str, balance:int):
        self.owner = owner
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += abs(amount)  # making sure it is positive

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= abs(amount)

    def print_details(self):
        # print(self.owner.names)
        self.owner.print_details()
        print(self.acc_no)
        print(self.balance)
        print("-----------------")


owner1 = Client("Jane Njeri", "A008", "1990-06-12", "F", "jane@gmail.com")
owner2 = Client("James Wafula", "B008", "1993-07-22", "M", "wafula@gmail.com")

acc1 = BankAccount(owner1, "12233", 67_800)
acc2 = BankAccount(owner1, "12244", 96_000)
acc3 = BankAccount(owner2, "12255", 99_000)

acc1.deposit(10_000)
acc1.deposit(7000)

acc1.print_details()
acc1.withdraw(15_000)
acc1.print_details()

print("Jane's age:", owner1.calc_age())
print("James' age:", owner2.calc_age())

print(acc1.owner.names, acc1.owner.calc_age())
print(owner1.names, owner1.calc_age())







# dob = "2003-02-23"
#
# today = date.today()
# print(today.year, today.month, today.day)
# # convert string to date
# birth_date = datetime.strptime(dob, "%Y-%m-%d")
#
# age = today.year - birth_date.year
# print(age)
#
# accurate_age = today - birth_date
# print(accurate_age)
