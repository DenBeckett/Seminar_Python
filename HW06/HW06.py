# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


a1 = int(input('Введите первый член прогрессии: ', ))
d = int(input('Введите шаг прогрессии: ', ))
n = int(input('Введите кол-во элементов прогрессии: ', ))
result_array = []
for i in range(1,n):
    result_array.append(a1 + (i - 1) * d)
print(result_array)

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)


from random import randint
n=int(input('Введите размер массива: '))
array=[randint(1,99) for _ in range(n)]
print(array)
min=int(input('Введите минимальное значение: '))
max=int(input('Введите максимальное значение: '))
result_array = []
for i in range(len(array)):
    if min <= array[i] <= max:
        result_array.append(i)
print(result_array)