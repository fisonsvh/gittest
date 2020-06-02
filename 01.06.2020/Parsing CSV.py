import os
from pandas import *
import pandas as pd

files = os.walk(r"C:\Users\User\Desktop\Examples")
list_of_files = []  # здесь хранятся пути к файлам
text_path = []  # здесь хранятся пути к файлам
for i in files:
    list_of_files.append(i)
    for i in list_of_files:
        for j in i[2]:
            text_path.append(i[0] + '/' + j)


def parsing_files(path):
    data = pd.read_csv(path)
    df = pd.DataFrame(data)
    print(df.describe())


for path in text_path:
    print(path.upper())
    parsing_files(path)

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
