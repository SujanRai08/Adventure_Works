# class Person:
#     number_of_people = 0
#     gravity = -9.8
#     def __init__(self,name):
#         self.name = name
#         Person.add_number()

#     @classmethod
#     def number_of_people_(cls):
#         return cls.number_of_people
#     @classmethod
#     def add_number(cls):
#         cls.number_of_people+=1

# p1 = Person('sujan')
# p2 = Person('sujan')
# print(Person.number_of_people_())

# static method  one def to anoher def
class Math:
    @staticmethod
    def add5(x):
        return x + 5
print(Math.add5(10))
