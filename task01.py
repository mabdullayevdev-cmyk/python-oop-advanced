class Car:
    count = 0
    cars = []

    def __init__(self, name, price):
        self.name = name
        self.price = price

        Car.cars.append(self)

    def get_info(self):
        return f"{self.name} {self.price}"

    @classmethod
    def create_object_from_dict(cls, data):
        return cls(data["name"], data["price"])

    @classmethod
    def get_expensive_car(cls):
        max_car = cls.cars[0]
        for car in cls.cars:
            if car.price > max_car.price:
                max_car = car
        return max_car

    @staticmethod
    def check_price(price):
        return price >= 0

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Car(name="{self.name}", price={self.price})'


Car("nexia", 4500)
Car("damas", 5500)
Car.create_object_from_dict({"name": "lacetti", "price": 6000})

print(Car.get_expensive_car().get_info())


# OOP: Inheritance, Polymophism, Abstruction, Encupsulation


# method, attr: public, private, protected


class BankAccount:

    __a = 0

    def __init__(self, name):
        self.name
        self.__balance = 0

        self.__balance

    def __get_balanace(self):
        pass

