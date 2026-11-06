from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        if radius < 0:
            raise ValueError("Radius manfiy bo'lmasligi kerak!")
        self.radius = radius

    def calculate_area(self) -> float:
        return math.pi * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        if width < 0 or height < 0:
            raise ValueError("O'lchamlar manfiy bo'lmasligi kerak!")
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base: float, height: float):
        if base < 0 or height < 0:
            raise ValueError("O'lchamlar manfiy bo'lmasligi kerak!")
        self.base = base
        self.height = height

    def calculate_area(self) -> float:
        return (self.base * self.height) / 2


if __name__ == "__main__":
    shapes = [
        Circle(5),
        Rectangle(4, 6),
        Triangle(3, 8)
    ]

    for shape in shapes:
        print(f"Area: {shape.calculate_area():.2f}")