class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product: Product, quantity: int):
        if product.quantity < quantity:
            raise ValueError("Omborda yetarli mahsulot yo'q!")
        self.items.append({"product": product, "quantity": quantity})

    def total_price(self) -> float:
        return sum(item["product"].price * item["quantity"] for item in self.items)


class Order:
    def __init__(self, customer, cart: ShoppingCart):
        self.customer = customer
        self.items = cart.items
        self.total_amount = cart.total_price()
        self.status = "PENDING"

        # Inventory'ni yangilash
        for item in self.items:
            item["product"].quantity -= item["quantity"]


class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


class Customer(User):
    def __init__(self, name: str, email: str):
        super().__init__(name, email)
        self.cart = ShoppingCart()

    def create_order(self) -> Order:
        return Order(self, self.cart)


class Admin(User):
    def add_product(self, inventory: list, product: Product):
        inventory.append(product)

    def remove_product(self, inventory: list, product: Product):
        if product in inventory:
            inventory.remove(product)