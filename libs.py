# # def get_count(string, symbol):
# #     cnt = 0;
# #     for i in string:
# #         if i == symbol:
# #             cnt = cnt + 1
# #     return cnt
# #
# #
# # def get_len(string):
# #     cnt = 0
# #     for i in string:
# #         cnt += 1
# #     return cnt
# #
# #
# # def len_name(name):
# #     return len(name)
#
# import random as r
#
# guess = r.randint (1, 10)
#
# while True:
#     question = int(input("Попробуй угадать число от 1 до 200. Вводи сюда число: "))
#     if question == guess:
#         anwser = input("Отлично, ты угадал! Хочешь сыграть еще?: ")
#         if anwser == 'д' or anwser == 'да':
#             guess = r.randint(1, 10)
#             continue
#         else:
#             print("Спасибо за игру!")
#             break
#     elif question < guess:
#         print('Загаданое число немного больше! Попробуй еще')
#     elif question > guess:
#         print('Загаданое число немного меньше! Попробуй еще!')

