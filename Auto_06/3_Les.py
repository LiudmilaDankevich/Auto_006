my_list = [1, 1, 1, 5, 5, 5, "Hello", 2.0, True, None]
print(my_list)
sentence = "Python is awesome"
print(sentence.split(' ', maxsplit=1))
print(my_list)
my_list[0] = 25
print(my_list)
print('after', my_list)
print(id(my_list))
# .APPEND()	МЕТОД ДЛЯ ДОБАВЛЕНИЯ ЭЛЕМЕНТОВ В СПИСОК
my_list.append(sentence)
print(my_list)
# .INSERT()	ДЛЯ ДОБАВЛЕНИЯ ЭЛЕМЕНТОВ В КОНКРЕТНОЕ МЕСТО В СПИСКЕ
my_list.insert(1, sentence)
# print(my_list)
# print(len(my_list))
# .INDEX()	ДЛЯ ПОЛУЧЕНИЯ ИНДЕКСА ЭЛЕМЕНТА
my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, [1, 2, 3, 4, 5]]
print(my_list1[-1][3])
# print(my_list.index("Hello"))
# .CLEAR()	ДЛЯ ОЧИСТКИ СПИСКА
# .REMOVE()	ДЛЯ УДАЛЕНИЯ ЭЛЕМЕНТА СПИСКА
# .REVERSE()	ЧТОБЫ РАЗВЕРНУТЬ СПИСОК В ОБРАТНОМ ПОРЯДКЕ
my_list1.reverse()
print(my_list1)
# .COUNT()	ДЛЯ ПОДСЧЕТА КОЛИЧЕСТВА ЭЛЕМЕНТОВ В СПИСКЕ
# print(my_list.count(5))
# SUM()	            ДЛЯ СЛОЖЕНИЯ ЭЛЕМЕНТОВ СПИСКА
# print(sum(my_list1))
# MIN()	            ПОКАЗЫВАЕТ ЭЛЕМЕНТ С САМЫМ НИЗКИМ ЗНАЧЕНИЕМ В СПИСКЕ
# print(min(my_list1))
# MAX()	            ЭЛЕМЕНТ С САМЫМ ВЫСОКИМ ЗНАЧЕНИЕМ В СПИСКЕ
# print(max(my_list1))
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for num in numbers:
    print(num*2)

n_list = [i for i in numbers if i % 2 == 0]
print(n_list)


# Кортежи
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
my_tuple1 = ("nos", )
print(my_tuple)
print(my_tuple1)
my_tuple2 = ("Anna", "Olga", "Mila")
print(my_tuple2)
a, b, c = my_tuple2
print(a)
print(b)
print(c)
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
my_list_n = list(my_tuple)
my_tuple3 = tuple(my_list_n)
print(my_list_n)
print(my_tuple3)

tuple1 = (1, 2, "Anna", "Olga", "Mila", 3, 4, 5, 6, 7, 8)
n_tuple = tuple([i for i in numbers if isinstance(i, int)])
t_tuple = tuple([i for i in numbers if isinstance(i, str)])
print(n_tuple)
print(t_tuple)


# .INDEX() — ИСПОЛЬЗУЕТСЯ ДЛЯ ВЫВОДА ИНДЕКСА ЭЛЕМЕНТА.
# .COUNT() — ИСПОЛЬЗУЕТСЯ ДЛЯ ПОДСЧЕТА КОЛИЧЕСТВА ЭЛЕМЕНТОВ В КОРТЕЖЕ.
# SUM() — СКЛАДЫВАЕТ ВСЕ ЭЛЕМЕНТЫ КОРТЕЖА.
# MIN() — ПОКАЗЫВАЕТ ЭЛЕМЕНТ КОРТЕЖА С НАИМЕНЬШИМ ЗНАЧЕНИЕМ.
# MAX() — ПОКАЗЫВАЕТ ЭЛЕМЕНТ КОРТЕЖА С МАКСИМАЛЬНЫМ ЗНАЧЕНИЕМ.
# LEN() — ПОКАЗЫВАЕТ КОЛИЧЕСТВО ЭЛЕМЕНТОВ КОРТЕЖА.
