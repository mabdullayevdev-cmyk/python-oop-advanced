class Employee:
    employee_count = 0

    def __init__(self, name: str, position: str, salary: float):
        if salary < 0:
            raise ValueError("Oylik manfiy bo'lishi mumkin emas!")
        self.name = name
        self.position = position
        self.salary = salary
        Employee.employee_count += 1

    def get_info(self) -> str:
        return f"{self.name} - {self.position} (${self.salary})"

    @classmethod
    def get_employee_count(cls) -> int:
        return cls.employee_count


if __name__ == "__main__":
    emp1 = Employee("Jasur", "Python Developer", 1500)
    emp2 = Employee("Malika", "UI/UX Designer", 1200)
    emp3 = Employee("Aziz", "Manager", 2000)

    print(emp1.get_info())
    print(f"Jami xodimlar soni: {Employee.get_employee_count()}")