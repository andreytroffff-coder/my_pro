'''n = [[1,2,3],[4,5,6],[7,8,9]]
print(*n,sep='\n')

# объявление функции
def is_pangram(text):
    f = True
    al = [chr(i) for i in range(ord('a'),ord('z')+1)]
    for i in range(len(al)):
        if al[i] not in text.lower():
            f = False
    return f

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))'''

'''import random
n = [i for i in range(1,101)]
print(random.choice(n))'''

'''numbers = list(map(int, input().split()))
cnt = 0
for i in range(len(numbers)):
    p = numbers[i]
    if numbers.count(p) == 1:
        cnt += 1
print(cnt)'''

# Пример вложенных циклов - таблица умножения
'''for i in range(1, 10):  # Строки
    for j in range(1, 8):  # Столбцы
        print(f"{i} × {j} = {i*j}", end="\t")
    print()'''  # Переход на новую строку после каждой строки таблицы

'''import os
print(f"Текущая директория: {os.getcwd()}")'''

'''import random 
print(random.random())'''

'''n = input()  
if len(n) == 5:
    n1 = n[::-1]
else:
    n1 =n[0]+n[-1:-len(n):-1]
print(int(n1))'''

'''import numpy as np
ar = np.arange(12)
print(ar.reshape(4,3))'''

'''

#n = [chr(i) for i in range(900,1500)]
#print(n)
n = 0
print(type(n))'''




'''import sympy as sp
x = sp.symbols('x')
function = x**2 + 3*x + 5
derivative = sp.diff(function, x)
print(derivative) '''

from pathlib import Path
print("Это текущая директория:", Path().home())
print("Это имя файла:", Path(r'C:\Users\Asus\Desktop\mypy\pytthon\решения'))
new = Path("folder")
new.mkdir()
#this version is for main



