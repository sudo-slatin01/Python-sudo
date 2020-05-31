"""
Дана строка, содержащая натуральные числа и слова.
Необходимо сформировать список из чисел, содержащихся в этой строке.
"""
s = '123 apple 345 banana'
word_list = s.split()
num_list = []
for word in word_list:
    if word.isnumeric():
        num_list.append(int(word))
print(f"Исходная строка: {s}")
print(f"Список чисел: {num_list}")

