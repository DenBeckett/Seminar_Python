# Задача №25. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# d g h t r g r h t j h b v f d s d f
# d g h t r g_2 r_2 h_2 t_2 j h_3 b v f d_2 s d_3 f_2
# Для решения данной задачи используйте функцию .split()


list = "d g h t r g r h t j h b v f d s d f"
splitted_list = list.split()
i = 0
for i in splitted_list:
    j = len(splitted_list) - i
    k = 1
    for j in splitted_list:
        if splitted_list[j] == splitted_list[i]:
            splitted_list[j] = f"{splitted_list[j]} + _ + {k}"
            k += 1
print(splitted_list)