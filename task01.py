class Student:
    university = "Tashkent University"

    def __init__(self, name: str, age: int, student_id: int):
        if age < 0:
            raise ValueError("Yosh manfiy bo'lishi mumkin emas!")
        self.name = name
        self.age = age
        self.student_id = student_id

    def get_info(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}"

    def is_adult(self) -> bool:
        return self.age >= 18


if __name__ == "__main__":
    student1 = Student("Ali", 22, 101)
    student2 = Student("Vali", 17, 102)
    student3 = Student("Zilola", 19, 103)

    print(student1.get_info())
    print(student2.is_adult())
    print(student3.is_adult())

    Student.university = "National University"
    print(student1.university)  

    student1.university = "TDIU"
    print(student1.university)  
    print(student2.university)  

    try:
        bad_student = Student("Sardor", -5, 104)
    except ValueError as e:
        print(f"Xatolik tutildi: {e}")