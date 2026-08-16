class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}.")


class Student(Person):

    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def introduce(self):
        super().introduce()
        print(f"I'm on course {self.course}.")


class Teacher(Person):

    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def introduce(self):
        super().introduce()
        print(f"I am professor {self.name}.")
        print(f"My subject is {self.subject}")


if __name__ == "__main__":
    print("Python")
    person = Person("Alice")
    person.introduce()

    print("\nPython")
    student = Student("Alice", 2)
    student.introduce()

    print("\nPython")
    student = Student("Alice", 2)
    student.introduce()
    teacher = Teacher("Bob", "Mathematics")
    teacher.introduce()
