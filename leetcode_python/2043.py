from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self._balance = balance
        self._account = len(balance) + 1

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self._judge(account1, money) and 0 < account2 < self._account:
            self._balance[account1 - 1] -= money
            self._balance[account2 - 1] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if 0 < account < self._account:
            self._balance[account - 1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self._judge(account, money):
            self._balance[account - 1] -= money
            return True
        return False

    def _judge(self, account, money):
        if 0 < account < self._account and self._balance[account - 1] >= money:
            return True
        return False


# Your Bank object will be instantiated and called as such:
balance = [10, 100, 20, 50, 30]
obj = Bank(balance)
param_1 = obj.transfer([5, 1, 20])
param_2 = obj.deposit([3, 10])
param_3 = obj.withdraw([5, 20])
