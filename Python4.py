"""
Допустим, дана строка слов, разделенных пробелами.
Необходимо найти в ней самое длинное слово и заменить в нем буквы 'a' на буквы 'b'.
"""
object = 'apple banana apple apple_banana'
string = object.split()
max = 0
for i in range(1, len(string)):
    if len(string[max]) < len(string[i]):
        max = i
helper = string[max]
print(f"Исходная строка: {object}")
print(f"Исправленная строка: {helper.replace('a', 'b')}")
