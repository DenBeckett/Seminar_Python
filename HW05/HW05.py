# Задача 26: 
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
3
# Input:
# A = 3; B = 5 -> 243 (3⁵)
# Output:
# A = 2; B = 3 -> 8

def get_exp(number1,number2):
    if number2 == 0:
        num = 1
    else:
         num = number1*get_exp(number1,(number2 - 1))
    return num

a = int(input())
b = int(input())
print(get_exp(a,b))

# Задача 28: 
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# Input:
# 2 2
# Output:
# 4

def get_sum(number1,number2):
    if number2 == 1:
        return number1 + 1
    else:
        return get_sum(number1 + 1,number2 - 1)
        

a = int(input())
b = int(input())
print(get_sum(a,b))