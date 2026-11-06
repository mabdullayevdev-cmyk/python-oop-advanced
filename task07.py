class EmployeeParent:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def get_info(self) -> str:
        return f"Name: {self.name}, Salary: ${self.salary}"


class Developer(EmployeeParent):
    def __init__(self, name: str, salary: float, programming_language: str):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def write_code(self) -> str:
        return f"{self.name} is writing code in {self.programming_language}."

    def get_info(self) -> str:
        return f"{super().get_info()}, Role: Developer, Lang: {self.programming_language}"


class Designer(EmployeeParent):
    def __init__(self, name: str, salary: float, design_tool: str):
        super().__init__(name, salary)
        self.design_tool = design_tool

    def create_design(self) -> str:
        return f"{self.name} is creating design using {self.design_tool}."

    def get_info(self) -> str:
        return f"{super().get_info()}, Role: Designer, Tool: {self.design_tool}"


class Manager(EmployeeParent):
    def __init__(self, name: str, salary: float, team_size: int):
        super().__init__(name, salary)
        self.team_size = team_size

    def manage_team(self) -> str:
        return f"{self.name} is managing a team of {self.team_size} members."

    def get_info(self) -> str:
        return f"{super().get_info()}, Role: Manager, Team Size: {self.team_size}"


if __name__ == "__main__":
    dev = Developer("Bekzod", 2500, "Python")
    des = Designer("Zarnigor", 1800, "Figma")
    mgr = Manager("Sanjar", 3000, 5)

    print(dev.get_info())
    print(dev.write_code())
    print(mgr.manage_team())