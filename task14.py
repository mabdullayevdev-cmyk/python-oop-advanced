class Person:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


class Student(Person):
    student_count = 0

    def __init__(self, name: str, email: str, student_id: str):
        super().__init__(name, email)
        self.student_id = student_id
        self.courses = []
        Student.student_count += 1

    @classmethod
    def create_student(cls, data: dict):
        return cls(data["name"], data["email"], data["student_id"])


class Teacher(Person):
    def __init__(self, name: str, email: str, subject: str):
        super().__init__(name, email)
        self.subject = subject


class Admin(Person):
    def manage_system(self) -> str:
        return "Admin is managing the university."