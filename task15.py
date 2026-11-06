from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    @abstractmethod
    def calculate_fare(self, distance: float) -> float:
        pass


class EconomyCar(Vehicle):
    def calculate_fare(self, distance: float) -> float:
        return distance * 1500


class BusinessCar(Vehicle):
    def calculate_fare(self, distance: float) -> float:
        return distance * 3000


class User:
    def __init__(self, name: str):
        self.name = name


class Passenger(User):
    def request_ride(self, destination: str, distance: float, vehicle: Vehicle):
        return Ride(self, destination, distance, vehicle)


class Driver(User):
    def __init__(self, name: str, vehicle: Vehicle):
        super().__init__(name)
        self.vehicle = vehicle
        self.is_available = True
        self.active_ride = None

    def accept_ride(self, ride):
        if not self.is_available:
            raise ValueError("Driver allaqachon boshqa safarda band!")
        self.is_available = False
        self.active_ride = ride
        ride.status = "ACCEPTED"


class Ride:
    def __init__(self, passenger: Passenger, destination: str, distance: float, vehicle: Vehicle):
        self.passenger = passenger
        self.destination = destination
        self.distance = distance
        self.vehicle = vehicle
        self.status = "PENDING"
        self.fare = vehicle.calculate_fare(distance)