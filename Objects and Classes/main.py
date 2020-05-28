from classes import Person

fison = Person('Vlad', 'Fisochenko')
tka4 = Person('Anton', 'Tkachenko')

fison.print_info()
tka4.print_info()

print(fison.get_age())

fison.set_age(20)

print(fison.get_age())
