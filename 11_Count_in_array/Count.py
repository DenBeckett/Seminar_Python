# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6


input_list = [1, 1, 2, 0, -1, 3, 4, 4]
output_list = []
count = 0
for item in input_list:
    if item not in output_list:
        count += 1
        output_list.append(item)
print(count)