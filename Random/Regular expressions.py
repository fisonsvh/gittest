import re

# s = 'Это просто строка текста. А это ее одна строка текста.'
# pattern = 'строка'

# if re.search(pattern, s):
#     print("Matched")
# else:
#     print("No matched")
#
# match = re.search(pattern, s)  # Matched
# print(match)  # <re.Match object; span=(11, 17), match='строка'>
# print(match.span())  # (11, 17)
# print(match.start())  # 11
# print(match.end())  # 17


# ______ Релугярные выражения регистрозависимы!______#


# match = re.match(pattern, s) # Поиск с самого начала строки
# print(match.span()) # (0, 3)

# ______Методы match and search ищут только одно совпадение_________#


# ______Метод findall находит все совпадения_________#

# match = re.findall(pattern, s)
# print(match)


# ______Разделение строки по шаблону_________# Точка – это метасимвол

# print(re.split(r'\.', s, 1))

# s = '''Это просто строка текста.
# А это ещё одна строка текста.
# А это строка с цифрами: 1, 2, 3, 4, 5, 6, 7, 8, 9, , 0, 10
# А это строка с разными символами: "!", "@", "-", "&", "?", "_"
# a\\b\tc
# test string'''

# pattern = r'\w+'
# pattern = r'[а-я0-9]+'
# pattern = r'[а-яё]+'
# pattern = r'[0-9]+'
# pattern = r'[\d]+'
# pattern = r'[\d-]+'
# pattern = r'[\d]+'


# print(re.findall(pattern, s, flags=re.IGNORECASE))

# ^ – Начало строки
# $ – Конец строки
# . – Любой символ
# + – Как минимум 1 символ
# (\w+\.) – Как минимум любой 1 символ
# {0,2}
#
#
#Fison23@gmail.com


def validate_email(email):
    return re.match(r'^[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$', email, re.IGNORECASE)

print(validate_email('Fison23@gmail.com'))