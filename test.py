
++++
"""
1. Дан массив, в котором среди прочих элементов есть слово "odd" (нечетный).
Определите, есть ли в списке число, которое является индексом элемента "odd". Напишите функцию, которая будет возвращать
True или False, соответсвенно.
"""


def odd_ball(arr):
    x = arr.index('odd')
    for i in arr:
        if int(x) in arr:
            return True
        else:
            return False


print(odd_ball(["even", 4, "even", 7, "even", 55, "even", 6, "even", 10, "odd", 3, "even"]))  # True
print(odd_ball(["even", 4, "even", 7, "even", 55, "even", 6, "even", 9, "odd", 3, "even"]))  # False
print(odd_ball(["even", 10, "odd", 2, "even"]))  # True

"""
3. Дан список имен. Выберите в новый список только те имена, которые состоят из 4-х букв.
["Ryan", "Mark", "John", "Paul"]
"""

names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"]
new_names = []
def get_names (names):
    for i in names:
        if len(i) == 4:
            new_names.append(i)
    print(new_names)

get_names(names)

"""
2. Напишите функцию find_sum(n), где аргумент функции - это конечный элемент последовательности включительно.
 Функция должна вернуть сумму всех чисел последовательности, кратных 3 или 5. Попробуйте решить задачу двумя способами (один из способов в одну строчку кода).
"""


def find_sum(n):
    l = list(range(1, n + 1))
    n = l[-1]
    b = []
    for i in l:
        if i % 3 == 0 or i % 5 == 0:
            b.append(i)
    print(b)
    return sum(b)


print(find_sum(10))
