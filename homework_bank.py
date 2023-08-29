class Account:

    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number
    
    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance
    
    def get_account_number(self):
        return self._account_number
    
    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'


class Savings_Account(Account):
    def __init__(self, balance, account_number, interest):
        super().__init__(balance, account_number)
        self.interest = interest

    def add_interest(self): # добавление ставки к общей сумме вклада
        interest =  self._balance * self.interest
        self._balance += int(interest)
        return self._balance
    
class Current_Account(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self.overdraft_limit = overdraft_limit

class Bank:
    def __init__(self, name: str) -> None:
        self.accounts = []
        self.name = name
        
    def update(self):
        for account in self.accounts:
            if isinstance(account, Savings_Account):
                account.add_interest()
            elif isinstance(account, Current_Account):
                if account.get_balance() > account.overdraft_limit:
                    print(f"Informing you about reaching overdaft limit on your account № {account.get_account_number()}")
                else:
                    print(f"Informing you that you didint reach overdaft limit on your account № \
{account.get_account_number()}, you can spend about {account.overdraft_limit - account.get_balance()}$ more")
    
    def open_account(self, account):
        self.accounts.append(account)
        
    def close_account(self, account):
        self.accounts.remove(account)
    
    def pay_dividend(self, dividend_sum):
        for account in self.accounts:
            account.deposit(dividend_sum)
    
    def show_all_acc(self):# тест для проверки что добавились/удалились необходимые счета, произведены операции 
        print(f'Opened accounts in {self.name.capitalize()}')
        for account in self.accounts:
            print(account)
       
        
monobank = Bank("monobank")
my_Account = Account(100000, 123456)
my_Savings_Account = Savings_Account(200000, 1234567, 0.2)
my_Current_Account = Current_Account(300, 123456789, 290)
other_Account = Account(100, 654321)
other_Savings_Account = Savings_Account(200, 7654321, 0.3)
other_Current_Account = Current_Account(300, 987654321, 1000)

# monobank.open_account(my_Account)
# monobank.open_account(my_Savings_Account)
# monobank.open_account(my_Current_Account)
# monobank.open_account(other_Account)
# monobank.open_account(other_Savings_Account)
# monobank.open_account(other_Current_Account)
# #monobank.show_all_acc()
# monobank.close_account(other_Savings_Account)
# monobank.show_all_acc()
# monobank.update()
# monobank.show_all_acc()
# monobank.update()
# monobank.pay_dividend(1999)
# monobank.show_all_acc()