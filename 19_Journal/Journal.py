# Задача №33.
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

import random
import time
journal = [random.randint(2, 5) for _ in range(10)]
maxx = max(journal)
minn = min(journal)
print(journal)
	
for ind in range(0, len(journal)):
	if journal[ind] == maxx:
	    journal[ind] = minn
print(journal)