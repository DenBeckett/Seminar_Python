# Задача №31.
# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

# Input: 7
# Output: 21

def fibonacci(num):
    if num == 0:
        fib = 0
    elif num == 1:
        fib = 1
    else:
        fib = fibonacci(num-1) + fibonacci(num-2)
    return fib

n = int(input())
for i in range(n):
    print(fibonacci(i))