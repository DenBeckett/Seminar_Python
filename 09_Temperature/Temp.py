# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел. Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2


max_count = 0
count = 0
n = int(input())
for _ in range(n):
    temp = int(input())
    if temp > 0:
        count += 1
    else:
        if count > max_count:
            max_count = count
        count = 0
if max_count == 0 and count != 0:
    print(count)
else:
    print(max_count)