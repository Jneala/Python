class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        
        def deposit(self, amount):
            balance += amount
            return amount
        def withdraw(self, amount):
            balance -= amount
            return amount
        def display_account_info(self, account):
            print("Balance: " + balance)
            
        def yield_interest(self):
            if balance > 0:
                balance = balance * int_rate
            return self


class User:
    def __init__(self, name, email, int_rate, account_balance):
        self.name = name
        self.email = email
        self.account_balance = account_balance
        self.checking = BankAccount(int_rate, self.account_balance)
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print(self.account_balance)
        return self
    
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self
    
user1 = User("Bob", "bob@bob.com")
user2 = User("Bob's Mom", "bobMom@bob.com")

user1.make_deposit(200)
user1.transfer_money(user2, 100)
# user2.display_user_balance()

user1.display_user_balance()
user1.make_deposit(100).make_withdrawal(5).transfer_money(user2, 50)
# user1.display_user_balance()
# user2.display_user_balance()