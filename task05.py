class Product:
    tax_rate = 0.12

    def __init__(self, name: str, price: float, quantity: int):
        if not self.is_valid_price(price):
            raise ValueError("Narx manfiy bo'lishi mumkin emas!")
        if quantity < 0:
            raise ValueError("Miqdor manfiy bo'lishi mumkin emas!")
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self) -> float:
        return self.price * self.quantity

    def apply_discount(self, percent: float):
        if not (0 <= percent <= 100):
            raise ValueError("Chegirma 0 va 100 oralig'ida bo'lishi kerak!")
        self.price -= self.price * (percent / 100)

    def price_with_tax(self) -> float:
        return self.total_price() * (1 + Product.tax_rate)

    @classmethod
    def change_tax_rate(cls, rate: float):
        if rate < 0:
            raise ValueError("Soliq stavkasi manfiy bo'lmasligi kerak!")
        cls.tax_rate = rate

    @staticmethod
    def is_valid_price(price: float) -> bool:
        return price >= 0


if __name__ == "__main__":
    p1 = Product("Laptop", 1000.0, 2)
    print(f"Total price: {p1.total_price()}")
    print(f"Price with tax: {p1.price_with_tax()}")

    p1.apply_discount(10)
    print(f"Price after 10% discount: {p1.total_price()}")