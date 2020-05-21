# def odd_ball(arr):
#     x = arr.index('odd')
#     for i in arr:
#         if int(x) in arr:
#             return True
#         else:
#             return False
#
# print(odd_ball(["even",4,"even",7,"even",55,"even",6,"even",10,"odd",3,"even"])) # True
# print(odd_ball(["even",4,"even",7,"even",55,"even",6,"even",9,"odd",3,"even"])) # False
# print(odd_ball(["even",10,"odd",2,"even"])) # True

#_______________________________________________________________________

# def find_sum (n):
#     n = list(range(1, n+1))
#     n = int(n)
#     print(n)
#         return sum(n)
#
# print(find_sum(5))


# 3. Дан список имен. Выберите в новый список только те имена, которые состоят из 4-х букв.
# ["Ryan", "Mark", "John", "Paul"]

names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"]
new_names = []
def get_names (names):
    for i in names:
        if len(i) == 4:
            new_names.append(i)
    print(new_names)

get_names(names)



