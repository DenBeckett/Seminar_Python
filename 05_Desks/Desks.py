# 3. В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. За каждой партой
#  может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. Выведите наименьшее число парт, которое нужно 
# приобрести для них.
# **Input:**
# 20
# 21
# 22
# **Output:**
# 32

print('Введите первое число: ')
class1 = int(input())
print('Введите второе число: ')
class2 = int(input())
print('Введите третье число: ')
class3 = int(input())


print(f"{(class1 + class2 + class3 + 1) // 2}")