""" #s = 'Hello World'
# if ' ' in s:
#    s = s.upper()
# else:
#    s = s.lower()

# print(s)


# def getsum(*args):
#    print(args)


#getsum ()
# # money_in_pocket = int(input("Enter, how much money do you have: "))
# # salary = int(input("Enter, how much money did you earn: "))
# # expences = int(input("Enter, how much money did you expence: "))
# # def my_money (money_in_pocket, salary, expences):
# #     return money_in_pocket + salary - expences
# #
# # print ('Your real money is:', my_money(money_in_pocket, salary, expences))
#
# # ____________________________
#
# # def my_money(money_in_pocket, salary, expences):
# #     return money_in_pocket + salary - expences
# #
# # print (my_money(20, 30, 10))
#
# # ____________________________
#
# # def say_hello (name, surname):
# #     print ('Hello, %s %s!' % (name, surname))
# # say_hello('Vlad', 'Fisochenko')
#
# # ____________________________
#
# # def my_function (my_salary, my_expences):
# #     return my_salary - my_expences
# #
# # print(my_function(100, 50))
#
# # ____________________________
#
# # def my_function ():
# #     firs_par = 50
# #     second_par = 20
# #     return firs_par * second_par
#
# # ____________________________
#
# # def space_ship (cans):
# #     all_cans = 0
# #     for time in range (1, 53):
# #         all_cans = all_cans + cans
# #         print('Week %s = %s cans!' % (time, all_cans))
# #
# # space_ship(4)
#
# # ____________________________
#
# # def space_ship(cans):
# #     week = 1
# #     while cans <= 1000:
# #         print('Week %s = %s cans' % (week, cans))
# #         cans = cans + 2
# # #         week = week + 1
# # #
# # # space_ship(2)
# #
# # # ____________________________
# #
# # # import time
# # # print(time.asctime())
# #
# # import sys
# #
# # def joke():
# #     print('How old are you?')
# #     age = int(sys.stdin.readline())
# #     if age < 10:
# #         print('No no no!')
# #     else:
# #         print('Yes Yes Yes!')
# # joke()
#
# # # ____________________________
#
# # def moon_weight (earth_weight, factor):
# #     for years in range(1, 50):
# #         earth_weight = earth_weight + factor
# #         print('At %s year your weight will be %s killos!' % (years, earth_weight))
# #
# # moon_weight(95, 5)
#
# # # ____________________________
#
# # def moon_weight (earth_weight, factor, step):
# #     step = step + 1
# #     for years in range(1, step):
# #         earth_weight = earth_weight + factor
# #         print('At %s year your weight will be %s killos!' % (years, earth_weight))
# # moon_weight(95, 5, 5)
#
# # # ____________________________
#
# # import sys
# #
# # print('Enter your start weight: ')
# # start_weight = int(sys.stdin.readline())
# # print('How your weight will be increase?: ')
# # factor = int(sys.stdin.readline())
# # print('How many years?: ')
# # years = int(sys.stdin.readline())
#
#
# # def moon_weight(start_weight, factor, years):
# #     for years_loop in range(1, years):
# #         start_weight = start_weight + factor
# #     print('In %s years your weight will be %s kilos!' % (years_loop, start_weight))
# #
# #
# # years = years + 1
# # moon_weight(start_weight, factor, years)
#
#
# # import sys
# #
# #
# # def moon_weight():
# #     print('Введи свой теперешний вес: ')
# #     start_weight = int(sys.stdin.readline())
# #     print('Введи число, на которое твой вес будет увеличиваться каждый год: ')
# #     factor = int(sys.stdin.readline())
# #     print('Введи количество лет: ')
# #     count_years = int(sys.stdin.readline())
# #     for years in range(1, count_years + 1):
# #         start_weight = start_weight + factor
# #         print('Через %s год твой вес составит %s килограм!' % (years, start_weight))
# #
# #
# # moon_weight()
#
# # class Girafe:
# #     reginald = Girafe()
# #     pass
#
#
# # class Toyota:
# #
# #     def __init__(self):
# #         self.color = 'red'
# #         self.price = '1 000 000'
# #         self. max_velocity = '200 km/h'
# #         self.current_velocity = '0 km/h'
# #         self.engine_pm = '0'
# #
# #     def start (self):
# #         print('Engined!')
# #         self.engine_pm = '900'
# #
# #     def go (self):
# #         print('You are started!')
# #         self.engine_pm = '2000'
# #         self.current_velocity = '20 km/h'
# #
# #
# # fisons_car = Toyota()
# #
# # fisons_car.go()
# # print('go', fisons_car.engine_pm)
# #
#
# # class Animals:
# #
# #     def garold_eat(self):
# #         print('Garold eating')
# #         pass
# #     def reginald_eat(self):
# #         print('Reginald eating')
# #         pass
# #
# # reginald = Animals()
# # garold = Animals()
# #
# # reginald.reginald_eat()
# #
# # garold.garold_eat()
#
# #_______________________________________________________
#
# #
# #     def __init__(self, marks):
# #         self.girafe_marks = marks
# #
# # osvald = Girafe(100)
# # print(osvald.girafe_marks)
#
# # class Girafe:
# #
# #     def left_leg_forward(self):
# #         print('Left leg forward!')
# #     def left_leg_backward(self):
# #         print('Left leg backward!')
# #     def right_leg_forward (self):
# #         print('Right leg forward!')
# #     def right_leg_backward (self):
# #         print('Right leg backward!')
# #     def dancing(self):
# #         self.right_leg_forward()
# #         self.left_leg_forward()
# #         self.right_leg_backward()
# #         self.left_leg_backward()
# #
# # robert = Girafe()
# #
# # robert.dancing()
# #
# # # robert.right_leg_backward()
# # # robert.right_leg_forward()
# # # robert.left_leg_forward()
#
# # numbers = int(input('Enter numbers: '))
# # my_list = []
# #
# # for x in range(1, numbers+1):
# #     x = int(input('ENTER: '))
# #     my_list.append(x)
# #     my_list.sort()
# #
# # for a in my_list:
# #     a = a * 10
# #     print(a)
#
# # from tkinter import  *
# # import random
# # import time
# #
# # tk = Tk()
# # tk.title("Game")
# # tk.resizable(0, 0)
# # tk.wm_attributes("-topmost", 1)
# # canvas = Canvas (tk, width=500, height=400, bd=0, highlightthickness=0)
# # canvas.pack()
# # tk.update()
# #
# # class Ball:
# #     def __init__(self, canvas, color):
# #         self.canvas = canvas
# #         self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
# #         self.canvas.move(self.id, 240, 100)
# #
# #     def draw(self):
# #         pass
# def poslat_tka4a_nahuy ():
#     tka4s_answer = input ("не хочу с тобой больше пиздеть ")
#     if tka4s_answer == 'Ты как баба':
#         print ('Пошел нахуй')
#     elif tka4s_answer == 'Но все равно ты как баба :)))':
#
# poslat_tka4a_nahuy ()
#
# from tkinter import *
# import random
# import time
#
# tk = Tk()
# tk.title('My Game')
# tk.resizable(False, False)
# tk.wm_attributes("-topmost", 1)
# canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0)
# canvas.pack
# tk.update()
# input()
#
# class Ball:
#     def __init__(self, canvas, color):
#         self.canvas = canvas
#         self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
#         self.canvas.move(self.id, 240, 100)
#
#     def draw(self):
#         pass
#
# l = ['1', '2', '3', 'four', 'five']
# names = ['Ivanov', 'Pertov', 'Sidorov']
#
# print(names[-1])

# import random
# import time
#
# number = int (input('How much number do you wanna put in list?: '))
# l_number = list(range(1, number + 1))
# random.shuffle(l_number)
# x = 1
# t_1 = time.time()
# for i in l_number:
#     print(x, 'number is ', i)
#     x = x + 1
# t_2 = time.time()
# print('Всего %s цифр в списке' % len(l_number))
# print('Время, потраченное на подсчет – %s '% int((t_2 - t_1)))

# list = ['hello', 'world', 'world', 'hello']
#
# print(list)
#
# n_list = list.pop()
#
# print(n_list)
#
# list = list(range(1, 500))
#
# list.count(1)
#
# print(list)
# print(list.count(700))

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# for x in a:
#     if x < 5:
#         print(x)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# result = list(set(a) & set(b))
#
# print(result)
# import random
#
# number = random.randint (1, 500)
# my_list = list(range(1, number + 2))
#
# for x in my_list:
#     if x % 2:
#         print(x)
#         if x == number:
#             break
# print('You\'ve got %s ! Bye bye!'% number)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# result = list(set(a) ^ set(b))
#
# print(result)


# my_str = 'Сложите цифры целого числа'
# print(my_str.count('и'))
#
# a, b = 2, 4
# a, b = b, a
#
# print(a, b)

# b = 'Обратите внимание, что у любой задачи по программированию может быть несколько способов решения. Чтобы посмотреть добавленный нами вариант решения, кликните по соответствующей кнопке. Все приведённые варианты написаны на Python 3.'
#
# print (max(b.split(), key=lambda i:len(i)))
#
#
#
#
#
# list = [2, 4, 8]
# new_list = []
# for x in list:
#     new_list.append(x * x)
#
# print(new_list, 'Sum is %s' % sum(int(new_list)))
# print(type(new_list))

# list = [2, 4, 8]
# new_list = []
# for x in list:
#     new_list.append(x * x)
#
# print(list)
# string_1 = 'Список в квадрате', new_list,'\n','Сумма всех элементов списка – %s' % sum(new_list)
# print(type(string_1))
# print(type(new_list)) """

#
# """ def get_sum(a, b):
#     return a + b
#
#
# print(get_sum(1, 5)) """
#
# """ a = 5
# def f ():
#     global a+=1
#     print ()
# print(a) """
#
# """ l = [1, 2, 3]
#
#
# def f(l):
#     return [i * 2 for i in l]
#
#
# print(f(l))
#  """
#
# #  l2 = [1, 2, 3, 4, 5, 6]
# # def f2(l)
# #     def get_mult (l2):
# #

#
# print(l.get_count('hello world', 'o'))
# print(l.get_len('hello'))
# print('Your name lens is %s' % l.len_name('Vlad'))

# import random as r
#
# mylist = list(range(1, r.randint(100, 500)))
# print(mylist)
#
# mylist2 = list(range(r.randint(200, 500), r.randint(100, 500)))
# print(mylist)
#
# mylist = set(mylist)
# mylist2 = set(mylist2)
#
# difference = (mylist - mylist2)
#
# x = 1
# for i in difference:
#     print(x, "difference is %s" % i)
#     x += 1
# # # # def get_count(string, symbol):
# # # #     cnt = 0;
# # # #     for i in string:
# # # #         if i == symbol:
# # # #             cnt = cnt + 1
# # # #     return cnt
# # # #
# # # #
# # # # def get_len(string):
# # # #     cnt = 0
# # # #     for i in string:
# # # #         cnt += 1
# # # #     return cnt
# # # #
# # # #
# # # # def len_name(name):
# # # #     return len(name)
# # #
# # # import random as r
# # #
# # # guess = r.randint (1, 10)
# # #
# # # while True:
# # #     question = int(input("Попробуй угадать число от 1 до 200. Вводи сюда число: "))
# # #     if question == guess:
# # #         anwser = input("Отлично, ты угадал! Хочешь сыграть еще?: ")
# # #         if anwser == 'д' or anwser == 'да':
# # #             guess = r.randint(1, 10)
# # #             continue
# # #         else:
# # #             print("Спасибо за игру!")
# # #             break
# # #     elif question < guess:
# # #         print('Загаданое число немного больше! Попробуй еще')
# # #     elif question > guess:
# # #         print('Загаданое число немного меньше! Попробуй еще!')
# #
# # from datetime import date, datetime
# # import locale
# #
# # #DATE CLASS
# #
# # # today = date.today()
# # # print(today)
# # # print(today.year)
# # # print(today.month)
# # # print(today.day)
# # # print(today.weekday())
# #
# # #DATETIME CLASS
# #
# # # today = datetime.now()
# # # today2 = datetime.today()
# # #
# # # print(today)
# # # print(today2)
# #
# # t = datetime.now()
# # t = t.timetuple()
# #
# # for i in t:
# #     print(i, end='-
#
# import os
# list = []
# tree = os.walk(r'C:\Users\User\PycharmProjects\gittest')
#
# for i in tree:
#     list.append(i)
#
# print(list)
#
# for adress, dirs, files in list:
#     for file in files:
#         print(adress+'/' + file)

# from datetime import date, datetime, time
# import time
#
# now = datetime.datetime.now()
#
# import colorama
#
# t = datetime.now()
# p = datetime.today()
#
# t = time.time()
# print(t)
#
# print(p)
# """
# 1. Дан массив, в котором среди прочих элементов есть слово "odd" (нечетный).
# Определите, есть ли в списке число, которое является индексом элемента "odd". Напишите функцию, которая будет возвращать
# True или False, соответсвенно.
# """
#
#
# def odd_ball(arr):
#     x = arr.index('odd')
#     for i in arr:
#         if int(x) in arr:
#             return True
#         else:
#             return False
#
#
# print(odd_ball(["even", 4, "even", 7, "even", 55, "even", 6, "even", 10, "odd", 3, "even"]))  # True
# print(odd_ball(["even", 4, "even", 7, "even", 55, "even", 6, "even", 9, "odd", 3, "even"]))  # False
# print(odd_ball(["even", 10, "odd", 2, "even"]))  # True
#
# """
# 3. Дан список имен. Выберите в новый список только те имена, которые состоят из 4-х букв.
# ["Ryan", "Mark", "John", "Paul"]
# """
#
# names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"]
# new_names = []
# def get_names (names):
#     for i in names:
#         if len(i) == 4:
#             new_names.append(i)
#     print(new_names)
#
# get_names(names)
#
# """
#
# 2. Напишите функцию find_sum(n), где аргумент функции - это конечный элемент последовательности включительно.
#  Функция должна вернуть сумму всех чисел последовательности, кратных 3 или 5. Попробуйте решить задачу двумя
#  способами (один из способов в одну строчку кода).
#
# """
#

#
# def find_sum(n):
#     l = list(range(1, n + 1))
#     n = l[-1]
#     b = []
#     for i in l:
#         if i % 3 == 0 or i % 5 == 0:
#             b.append(i)
#     print(b)
#     return sum(b)
#
#
# print(find_sum(10))


# def find_sum(n):
#     return sum(range(1, n))
#
#
# print(find_sum(5))
