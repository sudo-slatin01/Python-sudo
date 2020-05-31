import random
"""
Дано несколько списков с различным количеством элементов в каждом.
Для каждого списка найти максимум и разделить на него все элементы этого списка.
"""
list1, list2, list3 = [], [], []
for i in range(3):
    list1.append(round(random.random() * 100))
for i in range(5):
    list2.append(round(random.random() * 100))
for i in range(6):
    list3.append(round(random.random() * 100))
max1, max2, max3 = max(list1), max(list2), max(list3)
counter1, counter2, counter3 = 0, 0, 0
result1, result2, result3 = [], [], []
while counter1 < len(list1):
    result1.append(list1[counter1] / max1)
    counter1 += 1
while counter2 < len(list2):
    result2.append(list2[counter2] / max2)
    counter2 += 1
while counter3 < len(list3):
    result3.append(list3[counter3] / max3)
    counter3 += 1
print(f'Исходный спиок 1: {list1}\nИсходный спиок 2: {list2}\nИсходный спиок 3: {list3}')
print(f'Максимальный элемент списка 1: {max1}\nМаксимальный элемент списка 2: {max2}\nМаксимальный элемент списка 3: {max3}')
print(f'Получившийся список 1: {result1}\nПолучившийся список 2: {result2}\nПолучившийся список 3: {result3}\n')
