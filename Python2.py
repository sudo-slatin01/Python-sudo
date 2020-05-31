"""
Вводится строка. Необходимо определить в ней проценты прописных (больших) и строчных (малых) букв.
"""
def percents(mstr):
    uppers = lowers = 0
    for i in mstr:
        if i.isalpha():
            if i.islower():
                lowers += 1
            else:
                uppers += 1
    y = uppers + lowers
    x = (uppers*100)//y
    return {'upper':x,'lower':100-x};
print(percents(input('Введите строку:')))
