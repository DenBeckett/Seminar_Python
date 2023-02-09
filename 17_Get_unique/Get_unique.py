# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

# *Пример:* 

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

duplicates = [1, 2, 3, 5, 1, 5, 3, 10]
unique = duplicates[0:0]

for i in range(len(duplicates)):
    if duplicates[i] in unique: 
        continue
    unique.append(duplicates[i])

print(unique)