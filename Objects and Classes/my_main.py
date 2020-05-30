import random
from my_class import Person, Employee

student_1 = Person("Katy", 25)
student_2 = Person("Mike", 48)

student_1.greeting()
student_2.greeting()


employee = Employee("Peter", 44, 'Google')
employee.info()
print(employee)

