class Account():
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance
class Bank():
    def __init__(self):
        self.accounts = []
    def add_account(self, account):
        self.accounts.append(account)
        print("Account", account.account_no, "added")
    def remove_account(self, account):
        self.accounts.remove(account)
        print("Account", account.account_no, "removed")
    def calculate_balance(self):
        total_balance = sum(account.balance for account in self.accounts)
        return total_balance

account1 = Account("18889", 90000)
account2 = Account("09867", 70000)
account3 = Account("78971", 30000)

myBank = Bank()

myBank.add_account(account1)
myBank.add_account(account2)
myBank.add_account(account3)

total_balance = myBank.calculate_balance()
print("Total Balance in the bank:", total_balance)

myBank.remove_account(account3)

total_balance = myBank.calculate_balance()
print("Total Balance in the bank after account removal:", total_balance)