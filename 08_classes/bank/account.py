class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = int(balance)
        self.password =  password

    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print('Sorry! Incorrect password')
            print()
            return None
        
        if amountToDeposit <= 0:
            print('You cannot deposit negative amount')
            print()
            return None
        
        self.balance += amountToDeposit
        return self.balance

    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print('Sorry! incorrect password')
            print()
            return None
        if amountToWithdraw < 0:
            print('You cannot withdraw negative amount')
            print()
            return None
        
        if amountToWithdraw > self.balance:
            print('Sorry! You do not have enough money to withdow ')
            print()
            return self.balance
        
        self.balance -= amountToWithdraw
        return self.balance
    
    def transfarMoney(self, amountToTransfar, password):
        if password != self.password:
            print('Sorry! incorrect password try it again')
            print()
            return None

        if amountToTransfar <= 0:
            print('You cannot transfar negative amount')
            print()
            return None
        
        if amountToTransfar > self.balance:
            print('Sorry! You do not have enough money to transfar')
            print()
            return self.balance

        self.balance -= amountToTransfar   
        return self.balance     
        

    def getBalance(self, password):
        if password != self.password:
            print('Sorry! incorrect password')
            print()
            return None
        return self.balance
    

    def show(self):
        print('Name', self.name)
        print('Balance', self.balance)
        # print('Password', self.password)
        print()


a1 = Account("Drongo", 1000, 1234)
a1.show()

a1.deposit(5000, 1234)
a1.show()

a1 .withdraw(5000, 1234)
a1.show()

a1.transfarMoney(25000, 1234)
a1.show()

bal = a1.getBalance(1234)
print('Your current balance is: ', bal)
print()


a2 = Account("Yaska", 100000, 5678)
a2.show()

a2.deposit(500000, 5678)
a2.show()

a2 .withdraw(50000, 5678)
a2.show()

a2.transfarMoney(10000, 5678)

bal = a2.getBalance(5678)
print('Your current balance is: ', bal)
