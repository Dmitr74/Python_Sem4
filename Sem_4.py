# Задача 22: 
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# some_list = [random.randint(1, 10000) for i in range(10 ** 7)]
# some_set = set(some_list)

import random

n = int(input ("Введите количество чисел в первом списке: "))
list_n = [random.randint (1, 100) for i in range(n)]
print (list_n)
set_n = set(list_n)
print (set_n)

m = int(input ("Введите количество чисел во втором списке: "))
list_m = [random.randint (1, 100) for j in range (m)]
print (list_m)
set_m = set(list_m)
print (set_m)

set_x = set_n.intersection(set_m)
list_x = list(set_x)
print (list_x)