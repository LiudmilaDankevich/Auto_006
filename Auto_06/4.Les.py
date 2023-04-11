import l as l

# Пример лямбда-функции.
double = lambda x: x*2
print(double(5))


my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)

l = [20, 'str', 15, 10, 'yes', 'apple', 48, 40.5]
l1 = [1, 20, 58, 46]
power = list(map(lambda x: x**2 if isinstance(x, int) else x, l))
print(power)
from functools import reduce
result = reduce(lambda x, y: x * y, l1)
print(result)
# Decarator
def my_decarator(func):
    def wrapper(arg):
        print("обертка")
        func(arg)
        print("завернули")
    return wrapper
@my_decarator
def say_name(name):
    print(f"Hello {name}")

say_name("Mila")
import datetime
bdate = 1980
current_date = datetime.date.today()
age = current_date.year - bdate
print(age)