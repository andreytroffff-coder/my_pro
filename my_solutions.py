'''word = input() + ' запретил букву'
al = [chr(i) for i in range(ord('а'),ord('я')+1) if i != ord('ё')]
b = []
for t in range(len(al)):
    if al[t] in word:
        b.append(al[t])
for j in range(len(b)):
    if j == 0:
        print(word,b[0])
    if j >= 0 and len(word) >2:
        word = word.replace(b[j], '').strip('  ')
        print(word,b[j])'''

'''word = input() + ' запретил букву'
al = [chr(i) for i in range(ord('а'),ord('я')+1) if i != ord('ё')]
for t in range(len(al)):
    if t == 0:
        print(word, al[t])
    if al[t] in word and len(word) > 2:
        word = word.replace(al[t],'').strip('  ')
        print(word, al[t])
    else:
        continue'''

'''n = [i for i in input().split()]
n1 = []
k = []
for j in range(len(n)):
    if n[j] == n[j-1]:
        k.append(n[j-1])
        n1.append(k)
    else:
        n1.append(list(n[j]))
print(n1)'''

'''n, m = int(input()), int(input())
for i in range(n):
    for j in range(m):
        mult = i * j
        print(mult,end=" ")
    print()'''


#образец матрицы 
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# put your python code here
#f = open('t111.txt', 'r')

#p = f.readlines()
#print(p)

'''def int_r(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num
n = int(input())
cnt = 0
cnt1 = 0
d = set()
for i in range(n):
    m = input()
    if 'Correct' in m:
        cnt1 += 1
    d.add(m)
p = list(d)
for i in range(len(p)):
    if p[i][-7:] == 'Correct':
        cnt += 1 
if cnt != 0:
    print(f'Верно решили {cnt} учащихся\nИз всех попыток {int_r(cnt1/n*100)}% верных')  
else:
    print('Вы можете стать первым, кто решит эту задачу')'''

'''users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
t = []
for i in range(len(users)):
    if users[i]['phone'][-1] == '8':
        t.append(users[i]['name'])
print(*sorted(t))'''

'''import re
def check_password_strength(password):
    length = len(password) >= 8
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    digit = re.search(r"\d", password)
    special = re.search(r"[@$!%*?&]", password)

    if all([length, upper, lower, digit, special]):
        return "✅ Надёжный пароль"
    else:
        return "⚠️ Пароль слабый"
print(check_password_strength("Qwerty123"))
print(check_password_strength("Qw!8zYt@1"))'''

import numpy as np
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
anti_diagonal = np.fliplr(matrix).diagonal()
#print('Побочная диагональ:', anti_diagonal)

 
a = np.array([[1,2,3],[4,2,6]])
a1  = np.array([[1,2,3],[4,2,6],[1,5,2]]) #создание массива 
b = np.eye(5) #единичиная матрица
np.transpose(a) #транспонирование матриц
c = np.zeros((3,2)) #создание нулевой матрицы
np.matmul(a,a1)  #перемножение матриц 
np.dot(a,a1) 
print(np.dot(a,a1))

#генератор паролей длиной m и функция выводящие n паролей
import string
import random as rd
def generate_password(length):
    #s = [i for i in string.ascii_letters + string.digits if i not in 'lI0o1O']
    #l = [rd.choice([i for i in string.ascii_letters + string.digits if i not in 'lI0o1O']) for i in range(m)]
    return ''.join([rd.choice([i for i in string.ascii_letters + string.digits if i not in 'lI0o1O']) for i in range(m)])

def generate_passwords(count, length):
    for i in range(count):
        print(generate_password(length))

n, m = int(input()), int(input())
generate_passwords(n,m)

#МОЙ ПЕРВЫЙ ГЕНЕРАТОР ПАРОЛЕЙ
'''import string as stri
import random as rd
def generate_password(length):
    l = []
    s = [[i for i in stri.ascii_lowercase if i not in 'ol'], list(stri.digits[2:]), [i for i in stri.ascii_uppercase if i not in 'IO']]
    for k in range(m):
        if len(l) == m:
            break
        for i in range(3):
            l.append(rd.choice(s[i]))
            if len(l) == m:
                break
    rd.shuffle(l)
    return ''.join(l)
def generate_passwords(count, length):
    for i in range(count):
        print(generate_password(length))

n, m = int(input()), int(input())
generate_passwords(n,m)'''


