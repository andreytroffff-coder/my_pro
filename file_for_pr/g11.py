'''s = input()

def sh(s):
    if isinstance(s,list):
        return s[::-1]
    else:
        raise TypeError
print(sh(s))'''

# =============================================================================
# =============================================================================

'''import numpy as np
from numpy import linalg
a = np.array([[1,2],[4,2]])
a1  = np.array([[1,2,3],[4,2,6],[1,5,2]]) #создание массива 
b = np.eye(5) #единичиная матрица
np.transpose(a) #транспонирование матриц
c = np.zeros((3,2)) #создание нулевой матрицы
#np.matmul(a,a1)  #перемножение матриц 
#np.dot(a,a1) 
#print(a1)
det = np.linalg.det(a)
#print(a[1,0])   
arr = np.arange(1,100,2)
print(max(arr))'''

# =============================================================================
#проверка интерпретатора 
# =============================================================================
'''import sys
print(f"Версия: {sys.version}")
print(f"Интерпретатор: {sys.implementation.name}")
print(f"Путь: {sys.executable}")'''

'''from numpy import linalg
l = [[1,3],[5,6]]
print(linalg.inv(l))
'''

'''h = int(input())
m = int(input())
t = int(input())
if t >= 60:
	h += t // 60
	m += t % 60
if t < 60:
	m += t
if m >= 60:
	h += m // 60
	m += m % 60
if len(str(m)) < 2:
	m = str(m)
	m += '0'
print(h,':',m,sep='')'''

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

#еще генератор, но без обязат условия
'''import string
import random as rd
def generate_password(length):
    #s = [i for i in string.ascii_letters + string.digits if i not in 'lI0o1O']
    #l = [rd.choice([i for i in string.ascii_letters + string.digits if i not in 'lI0o1O']) for i in range(m)]
    return ''.join([rd.choice([i for i in string.ascii_letters + string.digits if i not in 'lI0o1O']) for i in range(m)])

def generate_passwords(count, length):
    for i in range(count):
        print(generate_password(length))

n, m = int(input()), int(input())
generate_passwords(n,m)'''
'''import dis
def f(x): return x * 3 + 1
dis.dis(f)
'''
'''import numpy as np
arr = np.array([1,2,5,6,4])
t =np.sum(arr, axis=0) #axis 0 это по столбцам, axis = 1 по строкам, но если одномерный массив то наооброт
p = np.eye(10,10)     
#print(np.max(arr, axis=0))
#print(p)
print(p) #первый срез относится к количеству или конкретной строкам (длина столбца),второй показывает количество столбцов (длину строки)
'''
'''import pandas as pd
s = pd.Series([1, 3, 5, 0, 6, 8])


df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Tokyo']
})
print(df.loc[0])'''



'''# Чтение одной строки из stdin
data = sys.stdin.readline()
print(f"Вы ввели: {data.strip()}")

# Чтение всего ввода до EOF
all_input = sys.stdin.read()
print(f"Весь ввод: {all_input}")'''


# Читаем ВСЕ данные сразу (не ждем пользователя)
#
# data = sys.stdin.read()
#print(f"Получены данные: {data}")

'''print("\n=== ИНФОРМАЦИЯ О ИНТЕРПРЕТАТОРЕ ===")

def interpreter_info():
    """Информация о интерпретаторе Python"""
    print(f"Реализация: {sys.implementation.name}")
    print(f"Версия реализации: {sys.implementation.version}")
    print(f"Версия Python: {sys.version_info}")
    print(f"Исполняемый файл: {sys.executable}")
    print(f"Префикс установки: {sys.prefix}")
interpreter_info()
print(sys.version)
    
print(f"\nЗагружено модулей: {len(sys.modules)}")
print("Последние 5 загруженных модулей:")
for name in list(sys.modules.keys())[:]:
     print(f"  {name}")'''

'''l1 = [str(i) for i in range(int(input()),int(input())+1)]
for i in range(len(l1)):
    if all(list(map(lambda x: True if x != 0 and int(l1[i]) % x == 0 else False, list(map(int, l1[i]))))):
        print(l1[i],end=" ")'''

'''n = int(input())
for i in range(n):
    l = int(input())
    for j in range(l):
        d = {k:v  for k,v in input().split()} 
print(d)'''

'''import mysql.connector 
dataBase =  mysql.connector.connect(
  host ="localhost",                # Localhost for local connection
  user ="root",
  passwd ="0909egor0909",
  database = "sakila")

cursorObject = dataBase.cursor()
 
query = "select * from actor"
cursorObject.execute(query) 
  
myresult = cursorObject.fetchall() 
for x in myresult:
    print(x)

dataBase.close()'''

'''import numpy as np
# модуль нужен для считывания файлов из стандартного потока
import sys

# считывание из стандартного потока ввода
data = np.loadtxt(sys.stdin, dtype = int)
t = np.sum(data, axis=1)
print(t)'''


import sys
#df = pd.read_csv(sys.stdin)
#print(*df[df['Возраст'] > 35]['Имя'].to_list())

#df = pd.read_csv(sys.stdin)
#p = df[df['brand'] == 'chevrolet']['price'].mean()

#df = pd.read_csv(sys.stdin)
#p = df[['brand','color']].drop_duplicates()
#c = p.groupby('brand')['color'].count()
#print(c.to_dict())


#df = pd.read_csv(sys.stdin)
#groped = df.groupby('Domains')['Name'].nunique().count()
#mx = groped.max()
#d = groped[groped == mx].to_dict()
#for k,v in d.items():
#    print(k, v)

#df = pd.read_csv(sys.stdin)
#l = df['Year Published'].apply(lambda x: 2021-int(x)).mean()
#print(round(l,2)) 

#df = pd.read_csv(sys.stdin)
#l = df[df['Domains'] == 'Strategy Games']['Rating Average'].apply(lambda x: float(x.replace(',','.'))).mean()  
#print(round(l,2)) 

'''import screen_brightness_control as sbc
current = sbc.get_brightness()
print("Текущая яркость:", current)
s = int(input())
if 0 <= s <= 100:
    sbc.set_brightness(s)  # уровень 0–100
    print("Яркость изменена")
else: 
    print('Неправильное число')
'''

'''from datetime import datetime

data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'), 
        'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'), 
        'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'), 
        'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'), 
        'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'), 
        'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'), 
        'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'), 
        'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'), 
        'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'), 
        'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'), 
        'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}
l = {datetime.strptime(v[-1], '%d.%m.%Y %H:%M:%S').timestamp() - datetime.strptime(v[0], '%d.%m.%Y %H:%M:%S').timestamp():k for k, v in data.items()}
print(l[min(l)])'''

#import os
#print(os.getcwd())

'''from datetime import datetime 
with open('diary.txt', encoding='utf-8') as file:
    dr = {datetime.strptime(i[:i.find('\n')], '%d.%m.%Y; %H:%M'):i[i.find('\n'):] for i in file.read().split('\n\n')}
    t = {key:dr[key] for key in sorted(dr)}
    for k, v in t.items():
        print(f'{k.strftime('%d.%m.%Y; %H:%M')}{v}\n')


from datetime import datetime 
with open('diary.txt', encoding='utf-8') as file:
    dr = {}
    l = file.read().split('\n\n')
    for i in l:
        dt = i[:i.find('\n')]
        tt = i[i.find('\n'):]
        dr.setdefault(datetime.strptime(dt, '%d.%m.%Y; %H:%M'),tt)
    keys = list(dr.keys())
    keys.sort()
    t = {key:dr[key] for key in keys}
    for k, v in t.items():'''

'''from datetime import datetime
start, end = datetime(year=1, month=1, day=1).toordinal(), datetime(year=9999, month=12, day=31).toordinal()
d = {k:0 for k in range(7)}
for i in range(start, end+1):
    if int(datetime.fromordinal(i).strftime('%d')) == 13:
        d[datetime.fromordinal(i).weekday()] += 1
print(*d.values(),sep='\n')
'''

import timeit

# Сравнение скорости разных подходов
code1 = """
from datetime import datetime, timedelta
dt = datetime.strptime(input(), '%d.%m.%Y %H:%M')
tm = timedelta(hours=dt.hour, minutes=dt.minute)
if 5 <= dt.weekday() <= 6:
    print(int((timedelta(hours=18)-tm).total_seconds()/60) if timedelta(hours=10) <= tm < timedelta(hours=18) else 'Магазин не работает')
else:
    print(int((timedelta(hours=21)-tm).total_seconds()/60) if timedelta(hours=9) <= tm < timedelta(hours=21) else 'Магазин не работает')
"""

code2 = """
from datetime import datetime, timedelta
dt = datetime.strptime(input(), '%d.%m.%Y %H:%M')
tm = timedelta(hours=dt.hour, minutes=dt.minute)
if 5 <= dt.weekday() <= 6:
    end = timedelta(hours=18)
    start = timedelta(hours=10)
    if start <= tm < end: 
        print(int((end-tm).total_seconds()/60))
    else: 
        print('Магазин не работает')
else:
    end = timedelta(hours=21)
    start = timedelta(hours=9)
    if start <= tm < end: 
        print(int((end-tm).total_seconds()/60))
    else: 
        print('Магазин не работает')
"""

from datetime import *
print(datetime.today().date())

def get_days_in_month(year, month):
    import calendar as cd
    from datetime import date
    mn = cd.monthrange(year, list(cd.month_name).index(month))[1]
    ls = sorted([date(year=year, month=list(cd.month_name).index(month), day=i) for i in range(1, mn+1)])
    return ls 

def get_all_mondays(year):
    import calendar as cd
    from datetime import date
    ls = [[date(year=year, month=j, day=i) for i in range(1,cd.monthrange(year, j)[1]+1) if cd.weekday(year, j, i) == 0] for j in range(1, 13) ] 
    l = []
    for i in ls:
        l.extend(i) 
    return sorted(l)

import time

st1 = time.monotonic()
import csv 
#with open('sales.csv', encoding='utf-8') as file:
    #data = csv.DictReader(file, delimiter=';' )
    #for r in data:
    #  if int(r['old_price']) > int(r['new_price']):
    #    print(r['name'])
end1 = time.monotonic()

st2 = time.monotonic()    

#df = pd.read_csv('sales.csv', delimiter=';')
#names = df[df['old_price'].astype('int64') > df['new_price'].astype('int64')]['name']
#print(*names.tolist(),sep='\n')
end2 = time.monotonic()


#print('Time od csv-code:', end1-st1, 'Time of pandas-code:', end2-st2)


'''with open('salary_data.csv', encoding='utf-8') as file:
    data = csv.reader(file, delimiter=';' )
    next(data)
    d = {}
    for r in data:
        d.setdefault(r[0], []).append(int(r[1]))
        # в этом случаи 
    sal = {k:sum(v)/len(v) for k, v in d.items()}
    print(sorted(sal, key=lambda name: (sal[name], name)))'''
        
import csv 
'''n = int(input())-1
with open('deniro.csv', 'r', encoding='utf-8') as file:
    data = csv.reader(file)
    l = sorted([i for i in data], key=lambda x: int(x[n]) if x[n].isdigit() else x[n])
    for i in l:
        print(*i, sep=',')'''
    
    
def csv_columns(filename):
    import csv 
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        d = {}
        for r in reader:
            names = list(r.keys())
            for name in names:
                d.setdefault(name, []).append(r[name])
        return d 
    


'''import csv 
from collections import Counter
with open('data.csv', 'r', encoding='utf-8') as file:
    data = csv.DictReader(file)
    domains = dict(Counter([i['email'][i['email'].index('@')+1:] for i in data]))
    sorted_d = dict(sorted(domains.items(), key=lambda x: (x[1], x[0])))

with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    heads = ['domain', 'count']
    writer.writerow(heads)
    for k, v in sorted_d.items():
        d = [k,v]
        writer.writerow(d)'''

'''import csv
with open('wifi.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    d = {}
    for r in reader:
        dis = r['district']
        d[dis] = d.get(dis, 0) + + int(r['number_of_access_points'])
    sorted_d = dict(sorted(d.items(), key=lambda x: (-x[1],x[0])))
    for k, v in sorted_d.items():
        print(f'{k}: {v}')'''
    
'''import csv 
with open('titanic.csv', 'r', encoding='utf-8') as file:
    data = csv.DictReader(file, delimiter=';')
    d = {}
    for row in data:
        if row['survived'] in '1' and float(row['age']) < 18:
            d.setdefault(row['name'], row['sex'])
    l = [k for k,v in d.items() if v == 'male'] + [k for k,v in d.items() if v == 'female']
    print(*l, sep='\n')'''

'''import csv
from datetime import datetime as dt 
with open('name_log.csv', 'r', encoding='utf-8') as file:
    data = csv.DictReader(file)
    d = {}
    for row in data:
        d.setdefault(row['email'], (row['username'], dt.strptime(row['dtime'], '%d/%m/%Y %H:%M')))
    
    em = sorted(d.keys())
    for row in data:
        if row['email'] in em:
            if dt.strptime(row['dtime'], '%d/%m/%Y %H:%M') >= d[row['email']][-1]:
                d[row['email']][-1] = dt.strptime(row['dtime'], '%d/%m/%Y %H:%M')
    d1 = {k:d[k] for k in em}
    


import pandas as pd
df = pd.read_csv('name_log.csv')
cols = list(df.columns)
df['dtime'] = df['dtime'].apply(lambda x: dt.strptime(x, '%d/%m/%Y %H:%M'))
d = df.groupby(['username','email']).agg({'dtime': 'max'})
d.to_csv('new_name_log.csv', index=False)


import pandas as pd   
df = pd.read_csv('name_log.csv')
    
    # Преобразуем строку даты в datetime для корректного сравнения
df['dtime_datetime'] = pd.to_datetime(df['dtime'], format='%d/%m/%Y %H:%M')
    
    # Сортируем по email и дате (по убыванию)
    # Таким образом для каждого email самая свежая запись будет первой
df_sorted = df.sort_values(by=['email', 'dtime_datetime'], 
                               ascending=[True, False])
print(df_sorted)    
    # Группируем по email и берем первую запись (самую свежую)
latest_df = df_sorted.groupby('email').first().reset_index()
print(latest_df)    
    # Оставляем только нужные колонки и сортируем по email
result_df = latest_df[['username', 'email', 'dtime']].sort_values('email')
print(result_df)    
    # Сохраняем результат
result_df.to_csv('new_name_log.csv', index=False)'''


def condense_csv(filename, id_name):
    import csv
    with open(filename, 'r', encoding='utf-8') as file, open('condensed.csv', 'w', encoding='utf-8', newline='') as out:
        data = csv.reader(file)
        cols = [id_name]
        d = {}
        for s in data:
            if s[1] not in cols:
               cols.append(s[1])
               d.setdefault(s[0], []).append(s[-1])
            else: 
                d.setdefault(s[0], []).append(s[-1])
        writer = csv.writer(out)
        writer.writerow(cols)
        for k,v in d.items():
            writer.writerow([k, *v])


'''text = 01,Artist,Otis Taylor
01,Title,Ran So Hard the Sun Went Down
01,Time,3:52
02,Artist,Waylon Jennings
02,Title,Honky Tonk Heroes (Like Me)
02,Time,3:29

with open('data.csv', 'w', encoding='utf-8') as file:
    file.write(text)

condense_csv('data.csv', id_name='ID')

with open('condensed.csv', encoding='utf-8') as file:
    print(file.read().strip())'''

from pathlib import Path

'''with open(Path('student_counts.csv'), encoding='utf-8') as file, open('sorted_student_counts.csv', 'w',encoding='utf-8', newline='') as out:
    d = csv.reader(file)
    cols = ['year'] + sorted([i for i in next(d) if i != 'year'], key=lambda x: (int(x[:-2]), x[-1:]))
    file.seek(0)
    data = csv.DictReader(file)

    writer = csv.writer(out)
    writer.writerow(cols)
    for i in data:
        row = [i[it] for it in cols]
        writer.writerow(row)'''

from datetime import datetime, timedelta
start = datetime(year=2026, month=1, day=19)
period = timedelta(weeks=6*4)
end = start + period

'''import json
with open('data.json', 'r', encoding='utf8') as file, open('updated_data.json', 'w', encoding='utf8') as out:
    data = json.load(file)
    l = []
    update_operations = {
    str: lambda x: f'{x}!',
    int: lambda x: x + 1,
    float: lambda x: x + 1,
    bool: lambda x: not x,
    list: lambda x: x * 2,
    dict: lambda x: x | {'newkey': None}
}
    for i in data:
        if i != None:
            l.append(update_operations[type(i)](i))
    json.dump(l, out, indent=3)'''


'''import json
with (open('people.json', 'r', encoding='utf8') as file,
      open('updated_people.json', 'w', encoding='utf8') as out):
    l = json.load(file)
    k = []
    res = []
    for dict in l:
        k.extend(dict.keys())
    k = set(k)
    for d in l:
        temp = {}
        temp = temp.fromkeys(k, None)
        temp.update(d)
        res.append(temp)
    
    json.dump(res, out, indent=3)'''

'''import json
with (open('countries.json', 'r', encoding='utf8') as file,
      open('religion.json', 'w', encoding='utf8') as out):
    data = json.load(file)
    res = {}
    for d in data:
        res.setdefault(d['religion'], []).append(d['country'])
    json.dump(res, out, indent=3)'''


'''import csv, json
with (open('playgrounds.csv', 'r', encoding='utf8') as file,
      open('addresses.json', 'w', encoding='utf8') as out):
    data = csv.DictReader(file, delimiter=';')
    d = {}
    for r in data:
        d.setdefault(r['AdmArea'],{}).setdefault(r['District'], []).append(r['Address'])
    json.dump(d, out, indent=3, ensure_ascii=False)'''

'''import csv, json
with (open('students.json', 'r', encoding='utf8') as file,
      open('data.csv', 'w', encoding='utf8', newline='') as out):
    data = json.load(file)
    writer = csv.writer(out)
    writer.writerow(['name','phone'])
    l = []
    for r in data:
        if r['age'] >= 18 and r['progress'] >= 75:
            l.append([r['name'], r['phone']])
    l.sort(key=lambda x: x[0])
    writer.writerows(l)'''

'''import json
from datetime import time, timedelta
with open('pools.json', 'r', encoding='utf8') as file:
    data = json.load(file)
    l = []
    for r in data:
        if 'Понедельник' in r['WorkingHoursSummer']:
            dt = r['WorkingHoursSummer']['Понедельник']
            start = datetime.strptime(dt[:dt.index('-')], '%H:%M').time()
            end = datetime.strptime(dt[dt.index('-')+1:], '%H:%M').time()
            if start <= time(hour=10) and end >= time(hour=12):
                l.append([r['DimensionsSummer']['Length'], r['DimensionsSummer']['Width'], r['Address']] )
    l.sort(key=lambda x: x[0], reverse=True)
    mx = max(l, key=lambda x: (x[0], x[1]))
    #print(f'{mx[0]}x{mx[1]}\n{mx[2]}')

import json, csv
from datetime import datetime
with (open('exam_results.csv', 'r', encoding='utf8') as file,
      open('best_scores.json', 'w', encoding='utf8') as out):
    data = csv.DictReader(file)
    l = set()
    res = {}
    for d in data:
        hs = d['email']
        if hs not in l:
            l.add(d['email'])
            res.setdefault(hs, []).extend([d['name'], d['surname'], d['score'], d['date_and_time']])
        else: 
            if int(d['score']) > int(res[hs][2]):
                res[hs][2] = d['score']
                res[hs][3] = d['date_and_time']
            elif int(d['score']) == int(res[hs][2]) and datetime.strptime(res[hs][3], '%Y-%m-%d %H:%M:%S') >  datetime.strptime(d['date_and_time'], '%Y-%m-%d %H:%M:%S'):
                res[hs][3] = d['date_and_time']
    js = []
    for i in res.items():
        hs = i[0]
        temp = {'name': i[1][0], 'surname': i[1][1], 'best_score': int(i[1][2]), 'date_and_time': i[1][3], 'email': hs}
        js.append(temp)
    js.sort(key=lambda x: x['email'])
    json.dump(js, out, indent=3)
        

    
import tracemalloc
import time

tracemalloc.start()
start = time.perf_counter()

#start of program
import csv
import json

result = {}
with open('exam_results.csv', encoding='utf-8') as ex_r:
    rows = csv.DictReader(ex_r)  # 1
    for row in rows:
        row['best_score'] = int(row.pop('score'))  # 2
        r = result.get(row['email'], row)  # 3
        best_row = max(r, row, key=lambda item: (item['best_score'], item['date_and_time']))  # 4
        result[row['email']] = best_row  # 5 

with open('best_scores.json', 'w', encoding='utf-8') as bs:
    out = sorted(result.values(), key=lambda item: item['email'])  # 6
    json.dump(out, bs, indent=3)  # 7
#end

current, peak = tracemalloc.get_traced_memory()
end = time.perf_counter()

print(f"Текущая память: {current / 1024 / 1024:.2f} MB")
print(f"Пиковая память: {peak / 1024 / 1024:.2f} MB")
print(f"Время выполнения: {end - start:.6f} секунд")

tracemalloc.stop()'''


'''with open('food_services.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    dis = {}
    for d in data:
        dis.setdefault(d['District'], []).append(1)
    dis = {k:sum(v) for k,v in dis.items()}
    mx1, dis1 = 0, ''
    for k, v in dis.items():   
        if v > mx1:
            mx1, dis1 = v, k

    di = {}
    mx2, dis2 = 0, ''
    for d in data:
        di.setdefault(d['OperatingCompany'], []).append(1)
    di = {k:sum(v) for k,v in di.items() if k != ''}
    for k, v in di.items():   
        if v > mx2:
            mx2, dis2 = v, k
    
    print(f'{dis1}: {mx1}\n{dis2}: {mx2}')'''

'''with open('food_services.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    dis = []
    for d in data:
        dis.append([d['Name'], d['TypeObject'], d['SeatsCount']])
    dis.sort(key=lambda x: (x[1], x[2]), reverse=True)
    d = {}
    for l in dis:
        d.setdefault(l[1], [l[0], l[2]])
    k = sorted(d.keys())
    for i in k:
        print(f'{i}: {d[i][0]}, {d[i][1]}')'''
    



'''from zipfile import ZipFile
with ZipFile('workbook.zip') as file:
    info = file.infolist()
    mem = [info[i].file_size for i in range(len(info))]
    com_mem = [info[i].compress_size for i in range(len(info))]
    print(f'Объем исходных файлов: {sum(mem)} байт(а)\nОбъем сжатых файлов: {sum(com_mem)} байт(а)')'''

''''import lmstudio as lms

# Use the top-level convenience API to interact with the default server (http://localhost:1234 by default)
model = lms.llm() 

# Generate a response
result = model.respond("Who are you, and what can you do?")
print(result)'''


'''
import os 
import zipfile as zp
from datetime import datetime
dt = datetime.strptime('2021-11-30 14:22', '%Y-%m-%d %H:%M')
res = []
with zp.ZipFile('workbook.zip') as file:
    for i in file.infolist():
        if datetime(*i.date_time) > dt and not i.is_dir():
            res.append(os.path.basename(i.filename))
    print(*sorted(res),sep='\n')

import zipfile as zp
from datetime import datetime
with zp.ZipFile('workbook.zip') as file:
    for i in file.infolist():
        if not i.is_dir():
            print(f'{os.path.basename(i.filename)}\n  Дата модификации файла: {datetime(*i.date_time)}\n  Объем исходного файла: {i.file_size} байт(а)\n  Объем сжатого файла: {i.compress_size} байт(а)\n')
'''
'''
import zipfile as zp
import json
def is_correct_json(string):
    import json
    try:
        return json.loads(string)
    except:
        return False
    
with zp.ZipFile('data.zip') as file:
    res = []
    for i in file.infolist():
        try:
            data =  file.read(i.filename).decode('utf8')
            d = is_correct_json(data)
            if d['team'] == 'Arsenal':    
                    name = (d['first_name'], d['last_name'])
                    res.append(name)    
        except:
            continue
    res = sorted(res, key=lambda x: (x[0], x[1]))
    for i in res:
        print(*i)
'''

'''import zipfile as zp
def convert_bytes(size):
    """Конвертер байт в большие единицы"""
    if size < 1000:
        return f'{size} B'
    elif 1000 <= size < 1000000:
        return f'{round(size / 1024)} KB'
    elif 1000000 <= size < 1000000000:
        return f'{round(size / 1048576)} MB'
    else:
        return f'{round(size / 1073741824)} GB'
with zp.ZipFile('desktop.zip') as file:
    data = [[i for i in row.filename.split('/') if i not in ''] for row in file.infolist()]
    for j in data:
        if len(j) == 1:
            print(*j)
'''

'''from zipfile import ZipFile

def get_size(size):
    res = ''
    if size != 0:
        if size < 1024:
            res = str(size) + ' ' + 'B'
        elif 1024 < size < 1024 ** 2:
            res = str(round(size / 1024)) + ' ' + 'KB'
        elif 1024 ** 2 < size < 1024 ** 3:
            res = str(round(size / 1024 ** 2)) + ' ' + 'MB'
        elif 1024 ** 3 < size:
            res = str(round(size / 1024 ** 3)) + ' ' + 'GB'

    return res

with ZipFile('desktop.zip') as zip_file:
    info = zip_file.infolist()    
    for i in info:
        name = [j for j in i.filename.split('/') if j != '']
        print(name)
        print('  ' * (len(name) - 1) + name[-1], get_size(i.file_size))

'''
import pathlib, os
p = Path().cwd() #os.getcwd()
mypy = Path(r'C:\Users\Asus\Desktop\mypy') 
print(mypy.stat().st_size, 'bytes')



from collections import Counter
import string
with open(r"C:\Users\Asus\Downloads\pythonzen.txt", 'r', encoding='utf8') as file:
    data = Counter([i.lower() for i in file.read() if i in string.ascii_letters])
    
       

import csv
with open(r"C:\Users\Asus\Downloads\name_log.csv", 'r', encoding='utf8') as file:
    data = csv.DictReader(file)
    res = Counter([row['email'] for row in data])


import os, csv, json
from collections import defaultdict

res = defaultdict(list)

with open(r"C:\Users\Asus\Downloads\quarter1.csv", 'r', encoding='utf8') as file:
    data = csv.reader(file)
    cols = next(data)
    for row in data:
        res[row[0]].extend(row[1:])

res = {k:sum(map(int, v)) for k,v in res.items()}
with open(r"C:\Users\Asus\Downloads\prices.json", 'r', encoding='utf8') as file:
    data = json.load(file)
    s = sum([data[k]*res[k] for k in data.keys()])
    print(s)

from calendar import day_name
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
days = {i: d for i, d in enumerate(map(str.title, day_name), 1)}
        

import sys
print(sys.version)









