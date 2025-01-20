# class Dog:
#     def __init__(self,name):
#         self.name = name

#     def speak(self):
#         print(f'hello my name is {self.name}')

# d = Dog('sujan')
# d.speak()
# print(d.name)


class students:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def average_age(self):
        return self.age
    
class Course:
    def __init__(self,coursename,max_enroll):
        self.coursename = coursename
        self.max_enroll = max_enroll
        self.students = []
    def add_students(self,student):
        if len(self.students) < self.max_enroll:
            self.students.append(student)
            return True
        return False
    
    def get_average(self):
        value = 0
        for student in self.students:
            value += student.average_age()
        return value/len(self.students)
        


s1 = students('sujan',20)
s2 = students('hari',40)

course = Course('science',2)
course = Course('science',3)
course.add_students(s1)
course.add_students(s2)
print(course.add_students(s2))
print(course.get_average())
