#
# def common (seq1, seq2):
#     list = []
#     for x in seq1:
#         if x in seq2:
#             list.append(x)
#     return list
#
# c1 = "SPAM"
# c2 = "SCAM"
# print(common(c1,c2))

# x = 88
# # def func():
# #     x = 99
# #     print(x)
# #
# # # func()
# # # print(x)
# import random as r
# import time
#
#
# def password(number):
#     y = None
#     l = []
#     time1 = time.time()
#     while number != y:
#         y = r.randint(1, 20)
#         l.append(y)
#     print('Твой пароль %s' % y)
#     time2 = time.time()
#     time3 = time2 - time1
#     print(f'Было подобрано %s вариантов' % len(l))
#     print('Затрачено %s секунд времени' % int(time3))
#
#
# password(500)
