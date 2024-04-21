
# Задача: Написать программу, которая из имеющегося массива строк формирует новый массив из строк,
# длина которых меньше, либо равна 3 символам.
# Первоначальный массив можно ввести с клавиатуры,
# либо задать на старте выполнения алгоритма.
# При решении не рекомендуется пользоваться коллекциями,
# лучше обойтись исключительно массивами.
#
# Примеры:
# [“Hello”, “2”, “world”, “:-)”] → [“2”, “:-)”]
# [“1234”, “1567”, “-2”, “computer science”] → [“-2”]
# [“Russia”, “Denmark”, “Kazan”] → []

original_arr = input("Введите текст для массива по одному. В случае отправки пустого значения ввод закроется: ")
my_arr = []
result_arr = []
while original_arr != '':
    my_arr.append(original_arr)
    original_arr = input("Введите текст для массива: ")

for word in my_arr:
    if len(word) <= 3:
        result_arr.append(word)

print(f"{my_arr} -> {result_arr}")