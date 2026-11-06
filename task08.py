class Vehicle:
    def __init__(self, brand: str, model: str, speed: float):
        if speed < 0:
            raise ValueError("Tezlik manfiy bo'lishi mumkin emas!")
        self.brand = brand
        self.model = model
        self.speed = speed

    def start(self) -> str:
        return f"{self.brand} {self.model} started."

    def stop(self) -> str:
        return f"{self.brand} {self.model} stopped."

    def accelerate(self, amount: float):
        if amount < 0:
            raise ValueError("Musbat son kiriting!")
        self.speed += amount

    def brake(self, amount: float):
        if amount < 0 or self.speed - amount < 0:
            raise ValueError("Tezlik 0 dan pastga tushib ketolmaydi!")
        self.speed -= amount

    def get_info(self) -> str:
        return f"{self.brand} {self.model}, Speed: {self.speed} km/h"


class Car(Vehicle):
    def __init__(self, brand: str, model: str, speed: float, number_of_doors: int):
        super().__init__(brand, model, speed)
        self.number_of_doors = number_of_doors

    def get_info(self) -> str:
        return f"{super().get_info()}, Doors: {self.number_of_doors}"


class Motorcycle(Vehicle):
    def __init__(self, brand: str, model: str, speed: float, has_sidecar: bool):
        super().__init__(brand, model, speed)
        self.has_sidecar = has_sidecar

    def get_info(self) -> str:
        return f"{super().get_info()}, Sidecar: {self.has_sidecar}"


class Truck(Vehicle):
    def __init__(self, brand: str, model: str, speed: float, load_capacity: float):
        super().__init__(brand, model, speed)
        self.load_capacity = load_capacity

    def get_info(self) -> str:
        return f"{super().get_info()}, Capacity: {self.load_capacity} tons"


if __name__ == "__main__":
    car = Car("Chevrolet", "Malibu", 60, 4)
    car.accelerate(40)
    print(car.get_info())