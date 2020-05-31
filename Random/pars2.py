# name = 'vlad fisochenko'

# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.title())
#
# print(f'{name.title()}, would you like to learn some Python today?')
# a, b, c = 1, 2, 3

#
# import this
# print(this)
#
# my_list = list(range(1, 5000+1))
# for n_x in my_list:
#     print(n_x)

# numbers = [x ** 3 for x in range(1, 10)]
# print(numbers)
# n = numbers
#
# numbers.append('4444')
# n.append('222')
# numbers.append('4444')
#
# print(n)

# pizzas = ['Mozzarella', 'Capri', '4 Cheeses']
# for names in pizzas:
#     print(f'I like {names.lower()} pizza')
# print('«I really love pizza!»')

# squares = [x for x in range(1, 102) if x % 2 == 0]
# for s in squares:
#     print(s, sep='\n')
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_numbers = numbers[:]
#
# numbers.append('10')
# new_numbers.append('11')
#
# print(numbers)
# print(new_numbers)

# my_pizzas = ['Mozzarella', 'Capri', '4 Cheeses']

# friend_pizzas = my_pizzas[:]
#
# my_pizzas.append('Ananasnaya')
# friend_pizzas.append('Barbeque')
#
# print('My favorite pizzas are: '.upper())
# for names in my_pizzas:
#     print(names)
#
# print('My friend’s favorite pizzas are: '.upper())
# for names in friend_pizzas:
#     print(names)


phone = 'Iphone'.lower()


print(phone == 'iphone')
import random as r


def simple_num (number):
    a = [x for x in number+1]


def primes(n):
    a = [0] * n  # создание массива с n количеством элементов
    for i in range(n):  # заполнение массива ...
        a[i] = i  # значениями от 0 до n-1

    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n:  # перебор всех элементов до заданного числа
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент простое число)
            while j < n:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1

    # вывод простых чисел на экран (может быть реализован как угодно)
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a
    return b

