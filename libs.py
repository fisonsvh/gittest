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

from datetime import date, datetime, time
import time

now = datetime.datetime.now()

import colorama

t = datetime.now()
p = datetime.today()

t = time.time()
print(t)

print(p)