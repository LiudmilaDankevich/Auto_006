
# Пример лямбда-функции.
double = lambda x: x*2
print(double(5))


my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)