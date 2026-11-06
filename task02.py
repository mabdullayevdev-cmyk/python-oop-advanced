class BankAccount:
    bank_name = "National Bank"

    def __init__(self, owner: str, balance: float, account_number: str):
        if balance < 0:
            raise ValueError("Boshlang'ich balans manfiy bo'lishi mumkin emas!")
        self.owner = owner
        self._balance = balance
        self.account_number = account_number

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit summasi musbat bo'lishi kerak!")
        self._balance += amount
        return self._balance

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Yechish summasi musbat bo'lishi kerak!")
        if amount > self._balance:
            raise ValueError("Hisobda yetarli mablag' mavjud emas!")
        self._balance -= amount
        return self._balance

    def get_balance(self) -> float:
        return self._balance

    def transfer(self, amount: float, target_account):
        if amount <= 0:
            raise ValueError("O'tkazma summasi musbat bo'lishi kerak!")
        if amount > self._balance:
            raise ValueError("O'tkazish uchun mablag' yetarli emas!")
        
        self._balance -= amount
        try:
            target_account.deposit(amount)
        except Exception as e:
            self._balance += amount 
            raise ValueError(f"Tranzaksiya muvaffaqiyatsiz tugadi: {e}")


if __name__ == "__main__":
    acc1 = BankAccount("Javohir", 1000.0, "ACC001")
    acc2 = BankAccount("Sardor", 500.0, "ACC002")

    acc1.deposit(200)
    print(f"Acc1 balance after deposit: {acc1.get_balance()}")

    acc1.transfer(300, acc2)
    print(f"Acc1 after transfer: {acc1.get_balance()}")
    print(f"Acc2 after transfer: {acc2.get_balance()}")

    try:
        acc1.withdraw(5000)
    except ValueError as e:
        print(f"Edge case xatoligi: {e}")