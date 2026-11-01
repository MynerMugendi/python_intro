class Customer:
    def __init__(self, names, dob, email, gender, kra):
        self.names = names
        self.dob = dob
        self.email = email
        self.gender = gender
        self.kra = kra

    def print_details(self):
        print(self.names)
        print(self.dob)
        print(self.email)
        print(self.gender)
        print(self.kra)


class Account:
    def __init__(self, acc_no, balance, owner):
        self.acc_no = acc_no
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        if amount <= 0:
            print("Please enter a positive amount")
        else:
            self.balance += amount
            print(f"Deposited: {amount}")

    def withdraw(self,amount):
        if amount <= 0:
            print("Please enter a positive amount")
        elif amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"withdrawal: {amount}")

    def print_details(self):
        print(self.acc_no)
        print(self.balance)
        self.owner.print_details()
        print("-------------")

owner1 = Customer("Victor Mugendi", "2006-12-13", "victormyner@gmail.com", "M", "D009")
owner2 = Customer("Barrack Muriithi", "2006-10-12", "barrack@gmail.com", "M", "W567U")
owner3 = Customer("Eric Mugambi", 2006-11-26,"shejidi@gmail.com", "M", "R45E")

bank_acc1 = Account(12233, 420_000, owner1)
bank_acc2 = Account(12244, 620_000, owner2)
bank_acc3 = Account(12255, 820_000, owner3)
bank_acc1.print_details()

bank_acc2.deposit(100_000)
bank_acc2.withdraw(200_000)
bank_acc2.print_details()


