# 1. Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно
# последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число).
# Протестируем функцию на файле «article.txt» со следующим содержимым:

# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

def read_last(lines, file):
    if type(lines) != int or lines <= 0:
        print('Введено неправильное количество строк')
    with open(file, 'r', encoding='utf-8') as file:
        text = file.read().splitlines()
        for el in range(len(text) - lines, len(text)):
            print(text[el])

lines = int(input('Введите количество строк: ', ))
read_last(lines, 'article.txt')



# 2. Документ «article.txt» содержит следующий текст:

# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину 
# (или список слов, если таковых несколько).

def longest_words(file):
    with open(file, 'r', encoding='utf-8') as file:
        text = file.read().splitlines()
        words = (" ".join(text)).split()
        count_dict = {}
        for el in words:
            count_dict[el] = len(el)

        # dict(map(reversed, count_dict.keys()))
        inv_count_dict = {}
        for k, v in count_dict.items():
            inv_count_dict[v] = inv_count_dict.get(v, []) + [k]
        
        count_max = 0
        for k in inv_count_dict.keys():
            if k > count_max:
                count_max = k
        
        print(inv_count_dict[count_max])


longest_words('article.txt')


# ДОП ЗАДАЧА.
# Классическая задача про бассейн, который заполняется через 3 трубы, слишком проста. У нас труб будет больше.
# Бассейн можно заполнить из N труб. В файле pipes.txt записаны времена заполнения всего бассейна только одной данной работающей трубой
# (в часах). Затем после пустой строки перечислены трубы, которые будут заполнять бассейн. Сколько минут на это потребуется?
# Номер трубы соответствует номеру строки, в которой записана ее производительность.
# Результат запишите в файл time.txt

# Ввод

# 1
# 2
# 3
# (пустая строка)
# 1 2 3

# Вывод
# 32.72727272727273



         