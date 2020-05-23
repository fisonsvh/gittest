# from datetime import date, time, datetime
# import locale
# # #
# # # now_d = date.today()
# # # now_t = datetime.now()
# # #
# # # dt = now_t.timetuple()
# # #
# # # dl = []
# # # for i in dt:
# # #     dl.append(i)
# # #
# # #
# # # print(dl)
# # # print(now_d)
# # # print(now_t)
# # #
# # # nn = now_t.strftime(("%A, %d. %B %Y %I:%M%p"))
# # #
# # # print(nn)
# # #
# # # sec = datetime.timestamp()
# #
# # now = datetime.today()
# #
# # n_h = now.hour
# # n_m = now.minute
# #
# #
# # print(n_h)
# # print(n_m)
# #
# #
# # def get_date_now ():
# #     now = datetime.today()
# #     return now.strftime(("%A, %d. %B %Y %I:%M%p"))
# #
# # print(get_date_now())
#
#
# now = datetime.now()
#
# n_d = now.day
#
# locale.setlocale(locale.LC_ALL, 'RU_ru')
#
# print(n_d)
#
# print(now.strftime("%A %d %B"))

import os

file_path = os.walk('libs.py')

for i in file_path:
    print(i)

print(i)
print(file_path)
