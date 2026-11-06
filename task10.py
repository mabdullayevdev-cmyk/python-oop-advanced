from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass


class CreditCardPayment(Payment):
    def pay(self, amount: float):
        if amount <= 0:
            raise ValueError("Summa musbat bo'lishi kerak!")
        print(f"Paid ${amount} successfully using Credit Card.")


class PayPalPayment(Payment):
    def pay(self, amount: float):
        if amount <= 0:
            raise ValueError("Summa musbat bo'lishi kerak!")
        print(f"Paid ${amount} successfully using PayPal.")


class CashPayment(Payment):
    def pay(self, amount: float):
        if amount <= 0:
            raise ValueError("Summa musbat bo'lishi kerak!")
        print(f"Paid ${amount} in Cash.")


if __name__ == "__main__":
    payments = [
        CreditCardPayment(),
        PayPalPayment(),
        CashPayment()
    ]

    for payment in payments:
        payment.pay(100.0)