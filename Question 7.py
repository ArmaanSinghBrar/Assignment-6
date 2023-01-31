class Student:
    pass

class Marks:
    pass

student1 = Student()
student2 = Student()
marks1 = Marks()
marks2 = Marks()

print(isinstance(student1, Student))  # True
print(isinstance(student2, Student))  # True
print(isinstance(marks1, Marks))  # True
print(isinstance(marks2, Marks))  # True

print(issubclass(Student, object))  # True
print(issubclass(Marks, object))  # True
