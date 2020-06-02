import os
from pandas import *
import pandas as pd

#############################################################
#############################################################
# files = os.walk(r"C:\Users\User\Desktop\Examples")
# list_of_files = []
# text_path = []  # здесь хранятся пути к файлам
# for i in files:
#     list_of_files.append(i)
#     for i in list_of_files:
#         for j in i[2]:
#             text_path.append(i[0] + '/' + j)
# print(text_path[0])
#############################################################
#############################################################

files = os.walk(r"C:\Users\User\Desktop\Examples")
list_of_files = [] # здесь хранятся пути к файлам
text_path = []  # здесь хранятся пути к файлам
for i in files:
    list_of_files.append(i)
    for i in list_of_files:
        for j in i[2]:
            text_path.append(i[0] + '/' + j)
print(text_path[0])

#############################################################
#############################################################
#
def parsing_files(path):
    data = pd.read_csv(path)
    df = pd.DataFrame(data)
    print(df)

for path in text_path:
    parsing_files(path)


#############################################################
#############################################################




#     fiiles = open(opening, 'r')
#
# data = fiiles.readlines()
# print(data)
# fiiles.close()


# gloss = {
#     'CSV': 'Comma separated values',
#     'SMM': 'Social media marketing',
#     'HTTP': 'Hyper text transfer protocol',
#     'HTML': 'Hyper text markup language'
# }
# x = 1
# for key, value in gloss.keys():
#     print(f'{x}. {key} - {value.capitalize()}')
#     x += 1

# my_person = {
#     'first': 'Vlad',
#     'last': 'Fisochenko',
#     'city': 'Kyiv',
#     'age': 25
#     }
#
# print(my_person)
# print(my_person['first'])
# print(my_person['last'])
# print(my_person['city'])
# print(my_person['age'])
#
# for name in my_person.values():
#     print(name)

#
# for key, value in my_person.items():
#     print(f"key : {key}")
#     print(f"value : {value}")

# list_of_nums = list(range(1, 11))
# for nums in list_of_nums:
#     if nums == 1:
#         print(str(nums) + 'st')
#     elif nums == 2:
#         print(str(nums) + 'nd')
#     elif nums == 3:
#         print(str(nums) + 'rd')
#     else:
#         print(str(nums) + 'th')
#
# users = ['Aaron', 'John', 'Aaron', 'Mike', 'Peter', 'Mike', 'Lily']
#
# for names in set(users):
#     print(f"{names} can use it!")


# # new_users = ['Vlad', 'Max', 'Peter', 'Alex', 'Lily']
# #
# #
# # for check in new_users:
# #     if check in current_users:
# #         print(f"{check} is not free. Choose another name!")
# #     else:
# #         print(f'Hello, {check}')
#
# # if users:
# #     for user in sorted(users):
# #         if user in users:
# #             users.remove(user)
# #         print(f"{user} removed!")
# # else:
# #     print("We need to ind some users!")
#
#
# # for user in users:
# #     if user == 'admin':
# #         print(f"Hello, {user}, would you like to see a status report?")
# #     else:
# #         print(f"Hello, {user}! Thank you for logging in again")

#
