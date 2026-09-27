class Student:
    def __init__(self, name, student_id, email, age, department):
        self.name = name
        self.student_id = student_id
        self.__email = None
        self.email = email
        self.age = age
        self.department = department

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Email must contain '@'.")
        self.__email = value

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print(f"Student type: {self.get_student_type()}")

    def calculate_result(self, *marks, bonus=0):
        if not marks:
            raise ValueError("Provide at least one mark.")
        if any(not 0 <= mark <= 100 for mark in marks):
            raise ValueError("Each mark must be between 0 and 100.")

        average = min(100, sum(marks) / len(marks) + bonus)

        if average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"

        return average, grade

    def get_student_type(self):
        return "Student"


class UndergraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, semester):
        super().__init__(name, student_id, email, age, department)
        self.semester = semester

    def get_student_type(self):
        return "Undergraduate Student"

    def display_info(self):
        super().display_info()
        print(f"Semester: {self.semester}")


class GraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, research_topic):
        super().__init__(name, student_id, email, age, department)
        self.research_topic = research_topic

    def get_student_type(self):
        return "Graduate Student"

    def display_info(self):
        super().display_info()
        print(f"Research topic: {self.research_topic}")


def main():
    students = [
        UndergraduateStudent(
            "Amina Rahman",
            "UG-1024",
            "amina@example.com",
            20,
            "Computer Science",
            semester=4,
        ),
        GraduateStudent(
            "Rafi Ahmed",
            "GR-2041",
            "rafi@example.com",
            25,
            "Computer Science",
            research_topic="Machine Learning in Healthcare",
        ),
    ]

    for student in students:
        print("=" * 40)
        student.display_info()
        print("Result (three marks):", student.calculate_result(88, 92, 84))
        print("Result (one mark plus bonus):", student.calculate_result(76, bonus=3))


if __name__ == "__main__":
    main()