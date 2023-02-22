# Примеры.

with open('les8test.txt', 'r', encoding='utf-8') as file:
    # text = file.read().splitlines()
    # print(text)

    while True:
        line = file.readline()
        if not line:
            break
        print(line.strip())


with open('filetest.txt', 'a', encoding='utf-8') as file:
    some_list = ['привет', 'пока']
    for word in some_list:
        file.write(word + '\n')

# Посчитать количество вхождений заданной буквы

n = input()
count = 0
with open('les8test.txt', 'r', encoding='utf-8') as file:
    text = file.read().splitlines()
    for el in text:
        for letter in el:
            if letter == n:
                count += 1
print(count)

import time

with open('les8test.txt', 'r', encoding='utf-8') as file:
    find_letter = input()
    count = 0
    start = time.time()
    for letter in file.read():
        if letter == find_letter:
            count += 1
    end = time.time()
    print(count)
    print(end - start)


with open('les8test.txt', 'r', encoding='utf-8') as file:
    find_letter = input()
    start = time.time()
    print(file.read().count(find_letter))
    end = time.time()
    print(end - start)

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint
n = int(input('Введите кол-во элементов в списке: '))
some_list = [randint(-n, n) for _ in range(n)]
print(some_list)
with open('les8test.txt', 'w', encoding='utf-8') as file:
    for _ in range(randint(1, n)):
        file.write(str(randint(0, n - 1)) + '\n')

with open('les8test.txt', 'r', encoding='utf-8') as file:
    mult = 1
    for ind in file.read().splitlines():
        mult *= some_list[int(ind)]
print(mult)