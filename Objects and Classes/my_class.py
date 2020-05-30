class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f'My name is {self.name}. I\'m {self.age} years old.')


class Employee(Person):

    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company

    def info(self):
        print(print(f'My name is {self.name}. I\'m {self.age} years old. '
                    f'I work at {self.company}!'))


    def __str__(self):
        return self.name
