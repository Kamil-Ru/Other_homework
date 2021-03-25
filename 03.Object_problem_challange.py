''' For this challenge, create a bank account class that has two attributes:

* owner
* balance

and two methods:

* deposit
* withdraw

As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn. '''


class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return'''Account owner:   {}
Account balance: {}'''.format(self.owner, self.balance)

    def deposit(self, deposit):
        
        self.balance += deposit
        print('Deposit Accepted')

    def withdraw(self, withdraw):

        if withdraw <= self.balance:
            self.balance -= withdraw
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')
        
acct1 = Account('Jose',100)

print(acct1)

print(acct1.owner)
print(acct1.balance)

acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)
        
# solution from UDEMY

class Account_2():

    def __init__(self,owner,balance):

        self.owner = owner
        self.balance = balance

    def deposit(self,dep_amt):

        self.balance = self.balance + dep_amt
        print(f'Added {dep_amt} to the balance')

    def withdraw(self,wd_amt):

        if self.balance >= wd_amt:
            self.balance = self.balance - wd_amt
            print("Withdrawal accepted")
        else:
            print("sorrry non enough fouds!")

    def __str__(self):
        return f'Owner: {self.owner} \nBalance: {self.balance}'
        
b = Account_2("Sam",500)
print(b.owner)
print(b.balance)
print(b)
b.deposit(100)
b.withdraw(600)
print(b)
        



    