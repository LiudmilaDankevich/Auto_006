# # 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
# my_list8 = ['a', 'b', [1, 2, 3], 'd']
# print(my_list8[2])
#
# my_list = ['a', 'b', [1, 2, 3], 'd']
# list9 = my_list[2]
# print(*list9, sep='\n')

# # 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# #    - получите сумму всех чисел,
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# #a) Using filter get sum of all integers
# print(sum(filter(lambda x: isinstance(x, int), list_1)))
# ------------------------------------------------------------------------
summ = 0
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
for i in list_1:
    if isinstance(i, int):
        summ += i
    elif isinstance(i, str) and 'a' in i:
        print(i)
print(summ)






# # -----------------------------------------------------------------------
# #    - распечатайте все строки, где есть буква 'a'
# #b) Using list comprehension print string which contain 'a'
# print([x for x in list_1 if isinstance(x, str) and 'a' in x])
# --------------------------------------------------------------------------
# 3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
# my_list1 = ['cat', 'dog', 'horse', 'cow']
# my_tuple = tuple(my_list1)
# print(my_tuple)
#----------------------------------------------------------------------------
# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
# family_1 = tuple(input('Введите текст через запятую: ').split(','))
# family_2 = tuple(input('Введите текст через запятую: ').split(' ', ))

# if len(family_1) > len(family_2):
#     print('family_1')
# if len(family_1) < len(family_2):
#     print('family_2')
# else:
#     print('Equal')

# if len(family_1) == len(family_2):
#     print('Equal')
# elif len(family_1) > len(family_2):
#     print('family_1')
# else:
#     print('family_2')
#--------------------------------------------------------------------------------------------------------------------
# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете
# передать информацию
#     о вашем любимом фил ьме.
film = {'title': 1, 'director': 2, 'year': 3, 'budget': 4, "main_actor": 5, 'slogan': '8'}
print(film)
#     - распечатайте только ключи
print(film.keys())
#     - распечатайте только значения
print(film.values())
#     - распечатайте пары ключ - значение
print(film)
# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# Option 1
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
result = 0
for x in my_dictionary:
    result += my_dictionary[x]
print(result)

# Option 2
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
print(sum(my_dictionary.values()))
#
# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
#
new_list = set([1, 2, 3, 4, 5, 3, 2, 1])
print(new_list)


# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
print(set1.intersection(set2))
#      - найдите значения, которые не встречаются в обоих множествах
print(set1.symmetric_difference(set2))
#      - проверьте являются ли эти множества подмножествами друг друга
print(set1.issubset(set2))
print(set2.issubset(set1))

# Option 2
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
print(sum(my_dictionary.values()))


