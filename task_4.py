class BankAccount:
    def __init__(self, number: str, balance: float, owner: str):
        self.number = number
        self.balance = balance
        self.owner = owner

    def deposit(self, amount: float) -> None:
        self.balance += amount
        print(f"Deposited {amount} to account {self.number}. New balance: {self.balance}")

    def withdraw(self, amount: float) -> None:
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.number}. New balance: {self.balance}")
        else:
            print("Insufficient funds!")

    def transfer(self, target_account: 'BankAccount', amount: float) -> None:
        if amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            print(f"Transferred {amount} from account {self.number} to account {target_account.number}.")
            print(f"New balance for account {self.number}: {self.balance}")
            print(f"New balance for account {target_account.number}: {target_account.balance}")
        else:
            print("Insufficient funds for transfer!")


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.accounts = []

    def get_total_balance(self) -> float:
        total_balance = sum(account.balance for account in self.accounts)
        return total_balance


account1 = BankAccount(number="123456", balance=1000.0, owner="John Doe")
account2 = BankAccount(number="789012", balance=1500.0, owner="Jane Doe")

person = Person(name="John", age=30)
person.accounts = [account1, account2]

account1.deposit(500.0)
account2.withdraw(200.0)

print(f"Total balance for {person.name}: {person.get_total_balance()}")
