class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f'this is {self.name} and my age is {self.age}')

class Dog(Pet):
    def __init__(self, name, age,color):
        super().__init__(name, age)
        self.color = color
    def speak(self):
        print( 'bark bark')
    def show(self):
        print(f'this is {self.name} and my age is {self.age} and my color is {self.color}')

class Cat(Pet):
    def speak(self):
        print( 'meow meow')

c = Dog('alia',9,'red')
c.show()
