# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# 5 -> 1 0 1 1 0
# 2

print('Введите число монеток')
n = int(input())
coins = []
i = 0
j = 0
for _ in range(n):
    coins.append(int(input()))
for _ in range(n):
    if coins[_] == 1:
        i += 1
    else:
        j += 1
if i > j:
    print(j)
else:
    print(i)


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y?1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3


print('Введите число S')
S = int(input())
print('Введите число P')
P = int(input())
for num1 in range(S-1):
    num2 = S - num1
    if num1*num2 == P:
        print(num1,num2)
        break

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# 10 -> 1 2 4 8

print('Введите число N')
N = int(input())
i = 0
b = 0
while b < N:
    b = 2**i
    if b < N:
        print(b)
        i += 1