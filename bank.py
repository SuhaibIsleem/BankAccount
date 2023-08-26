class Transactions:
    def __init__(self,type,amount):
        self.type = type
        self.amount = amount

    def print_transactions(self):
        print(f"Transaction Type:{self.type}\t|\tAmount:{self.amount}")

class BankAccount:
    def __init__(self,user,id):
        self.id = id
        self.user = user
        self.balance=0
        self.user_transactions = []

    def deposit(self,amount): # ايداع
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} completed successfully!\n>> Your Balance: {self.balance}")
            transaction = Transactions("Deposit",amount)
            self.user_transactions.append(transaction)
        else:
            print("Invalid amount !")


    def withdrawal (self,amount): # سحب
        if amount > 0 and amount <= self.balance :
            self.balance -= amount
            transaction = Transactions("Withdrawal", amount)
            self.user_transactions.append(transaction)
            print(f"Withdrawal of {amount} completed successfully!\n>> Your Balance: {self.balance}")

        else:
            print("Invalid amount !")


user = BankAccount("Ali",1)
user.deposit(5000)
user.withdrawal(100)
user.withdrawal(6000)



user2 = BankAccount("ahmed",2)
user2.deposit(10000)
user2.withdrawal(500)
user2.withdrawal(500)

print(f'List of transactions for user {user.user}:')
for t in user.user_transactions:
    t.print_transactions()
print("*" * 50)


print(f'List of transactions for user {user2.user}:')
for t in user2.user_transactions:
     t.print_transactions()
print("*" * 50)