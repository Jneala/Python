class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        
        def deposit(self, amount):
            balance += amount
            return self
        
        def withdraw(self, amount):
            balance -= amount
            return self
        
        def display_account_info(self, account):
            print("Balance: " + balance)
            
        def yield_interest(self):
            if balance > 0:
                balance += balance * int_rate
            return self


class User:
    def __init__(self, name, email, int_rate, balance):
        self.name = name
        self.email = email
        # self.account_balance = account_balance
        self.checking = BankAccount(int_rate, balance)
    
    def make_deposit(self, amount):
        self.checking.balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.checking.balance -= amount
        return self
    
    def display_user_balance(self):
        print(self.checking.balance)
        return self
    
    def transfer_money(self, other_user, amount):
        self.checking.balance -= amount
        other_user.checking.balance += amount
        return self
    
user1 = User("Bob", "bob@bob.com", .3, 200)
user2 = User("Bob's Mom", "bobMom@bob.com", .5, 100)

user1.make_deposit(200)
print(user1.checking.balance)
