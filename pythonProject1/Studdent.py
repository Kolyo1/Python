status_choices = ["in uni", "not in uni"]

class Person:
    def __init__(self, Fname, Lname, age, nation):
        self.Fname = Fname
        self.Lname= Lname
        self.age = age
        self.nation = nation

    def printPerson(self):
        return f"My name is {self.Fname} {self.Lname}. My age is {self.age}. I am from {self.nation}."

class Student(Person):
    def __init__(self,student_Id, status,fName, Lname, age, nation):
        super().__init__(fName,Lname,age,nation)
        self.student_Id = student_Id
        self.status = status
        self.courses = []

    def changeStatus(self, newStatus):
        self.status = newStatus

    def Student_data(self):
        return {
            "Student ID": self.student_Id,
            "Status": self.status,
            "Courses": self.courses
        }

    def set_course(self, course):
        self.courses.append(course)

    @staticmethod
    def create_group(students):
        group = []
        for student in students:
            group.append(student.Student_data())
        return group


student1 = Student("S001", "studing", "Alice", "Ahmed", "18","Bulgaria")
student2 = Student("S002", "work", "Bob", "Drob", "20","Turk")
student1.changeStatus("graduated")
student1.set_course("Mathematics")
student2.set_course("Physics")
print(student1.printPerson())
print(student1.Student_data())

group = Student.create_group([student1,student2])
print(group)