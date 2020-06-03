def garage(mark, model, **car_info):
    car_info['mark'] = mark
    car_info['model'] = model
    print(car_info)
    return car_info


car = garage('subaru', 'outback', wheels=4, color='blue', tow_package=True)
print(car)






# ingridients = []
# def sandwich(*args):
#     for i in args:
#         ingridients.append(i)
#         print(f"We added {i} to your sandwich")
#
# sandwich('mushrooms', 'tomato', 'broccoli')
# print(f'Your sandwitch has {len(ingridients)} ingridients')


# def making_pizza(*toppings):
#     for topping in toppings:
#         print(topping)
#
#
# making_pizza('mushrooms', 'cheese')


# frases = ['Hello, how are you?', 'Where are you from?', 'How old are you?']
# frases_removed = []
#
# def show_text(frases):
#     while frases:
#         for frase in frases:
#             deleted_frases = frases.pop()
#             frases_removed.append(deleted_frases)
#     print(frases)
#     print(frases_removed)
#
# show_text(frases[:])
#
# print(frases)
# print(frases_removed)


# def make_album(artist_name, album_name, year_of_release):
#     album_dict = {
#         'Artist name': artist_name,
#         'Album name': album_name,
#         'Year of release': year_of_release
#     }
#     print(album_dict)
#     return album_dict
#
# while True:
#     artist_name = input('Enter artist name >>>  ')
#     album_name = input('Enter album name >>>   ')
#     year_of_release = input('Enter year of release >>>   ')
#     make_album()
#     if artist_name == 'q' or album_name == 'q' or album_name == 'q':
#         break
#
#
#
#
#


# def make_album(artist_name, album_name, year=''):
#     album_dict = {
#         'Artist name': artist_name,
#         'Album name': album_name
#     }
#     print(f"Added artist name - {artist_name}")
#     print(f"Added album name - {album_name}")
#     if year:
#         album_dict['year'] = year
#     return album_dict
#
#
# print(make_album('Chemodan', "2012", year=2107))
# print(make_album('Drake', "Twist"))


# def city_country(city, country):
#     print(f'{city} {country}')
#
# city_country('Kyiv,', 'Ukraine')
# city_country('Rome,', 'Italy')
# city_country('Barcelona,', 'Spain')


# question_eat = input('Ты хочешь скушать пиццу? Введи "да" или "нет": \n').lower()
# while True:
#     if question_eat == 'нет':
#         print("Тогда я не понимаю, зачем ты пришел...")
#         break
#     elif question_eat == "да":
#         question_ingr = input("Что добавить в пиццу? (напиши 'стоп'> когда закончишь): \n").lower()
#         print(f"Добавлено >>> {question_ingr}")
#     if question_ingr == 'стоп':
#         break
# print("Спасибо, что зашли")
#

#
# def make_shirt (size = "L", text = "I love Python"):
#     print(f"Размер футболки {size}")
#     print(f"На футболке написано {text}")
#
# make_shirt(text="Huy")

# def formated_name(first, last, middle=""):
#     if middle:
#         full_name = f"{first} {middle} {last}"
#     else:
#         full_name = f"{first} {last}"
#     return full_name.title()
#
#
# person = formated_name('Joe', 'Doe')
# print(person)
