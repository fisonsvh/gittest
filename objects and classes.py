# class A:
#     property1 = 'Property1'
#     property2 = 'Property2'
#     name = 'guest'
#     def say_hi(self, name=''):
#         if name:
#             return 'Hi, ' + name + '!'
#         else:
#             return 'Hello, ' + self.name + '!'
#
#
#
#
# a = A()
# b = A()
#
# print(a.property1)
# print(a.property2)
# print(a.say_hi('Bob'))
# print(b.say_hi())

#____________________________________________

from classes import Person

person1 = Person('Petro')
person1.print_info()

person2 = Person('Mykola')
person2.print_info()
