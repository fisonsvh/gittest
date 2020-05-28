class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.__age = 30

    def print_info(self):
        print(f'Hello, my name is {self.name}! My surname is {self.surname}. I am {self.__age} years old.')

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if value in range(1, 100):
            self.__age = value
        else:
            print('Enter correct value')
