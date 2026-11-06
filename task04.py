class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius

    def to_fahrenheit(self) -> float:
        return self.celsius * 9 / 5 + 32

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        return celsius * 9 / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    temp = Temperature(25)
    print(f"25°C to Fahrenheit: {temp.to_fahrenheit()}")
    print(f"0°C to Fahrenheit (Static): {Temperature.celsius_to_fahrenheit(0)}")
    print(f"77°F to Celsius (Static): {Temperature.fahrenheit_to_celsius(77)}")