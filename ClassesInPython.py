#creating classes with Python

class Person:
    def __init__(self, name="", email="", phoneNumber=""):
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber

    def setName(self, name):
        self.name = name

    def setEmail(self, email):
        self.email = email

    def setPhone(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getPhone(self):
        return self.phoneNumber

    def __str__(self):
        return "Name: %s, Email: %s, Phone Number: %s" % (self.name, self.email, self.phoneNumber)


class Account:
    def __init__(self, account_number, balance, person= None):
        #using composition for Person member
        self.person = Person(person)
        self.account_number = account_number
        #balance will equal 0 if negative
        if balance < 0:
            balance = 0
        self.balance = balance

    def getAccount(self):
        return self.account_number

    def setPerson(self, person):
        self.person = person

    def getPerson(self):
        return self.person

    def getBal(self):
        #balance will equal 0 if negative
        if self.balance < 0:
            self.balance = 0
        return self.balance

    def setBal(self, b):
        if b < 0:
            b = 0
        else:
            self.balance = b


class Savings_Account(Account):
    def __init__(self, min_bal=100):
        Account.__init__(self, 8889, 150, person = None)
        self.min_bal= min_bal
        #value error if balance is below minimum balance
        if self.min_bal > self.balance:
            print("Error: Balance is lower than minimum balance")
            self.balance = self.min_bal

    def deposit(self, dep):
        self.balance += dep

    def withdraw(self, w):
        if self.balance - w < self.min_bal:
            print("Error: Unable to complete transcation")
        else:
            self.balance -= w

    def __str__(self):
        return "Balance: $%d" % (self.balance)

class Loan_Account(Account):
    def __init__(self, max_bal=3000):
        Account.__init__(self, 505, 0)
        self.max_bal = max_bal
        credit = (self.max_bal - self.balance)
        if self.balance > self.max_bal:
            print("Error: Unable to complete transcation")
            self.balance = self.max_bal

    def deposit(self, dep):
        self.balance -= dep

    def withdraw(self, withd):
        if self.balance > self.max_bal:
            print("Error: Unable to complete transcation")
            self.balance = self.max_bal
        else:
            self.balance += withd
        
    def __str__(self):
        return "Balance Due: $%s" % (self.balance)

#tests person class        
p = Person("Kelsey", "k@gmail.com", 2487662123)
p.setName("Tina")
p.setEmail("TinaB@gmail.com")
p.setPhone(2448821290)
print(p.getName())
print(p.getEmail())
print(p.getPhone())
print(p); print()

#tests account class
x = Account(888009, 2099, p)
x.setBal(-99)
print("Person: ",x.getPerson())
print("Your account number is:", x.getAccount())
print("Balance: $",x.getBal()); print()

#tests savings account class
s = Savings_Account(50)
s.setBal(100)
s.deposit(50)
print(s)
#tests to see if program will allow negative balance
s.withdraw(400)
s.withdraw(40)
print("Balance: $",s.getBal()); print()

#tests Loan class
l = Loan_Account(1000)
l.setBal(500)
l.deposit(300)
print("Balance afer deposit: $", l.getBal())
l.withdraw(250)
print("Balance after withdraw: $",l.getBal())
print(l)
