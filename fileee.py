import re 
with open(r'C:\Users\Asus\Desktop\mypy\pytthon\решения\nums.txt', 'r',encoding='utf-8') as file:
    n = 0
    #al = ''.join([chr(i) for i in range(ord('a'),ord('z')+1)])
    #l = list(map(lambda x: x.replace(al, ' '), file.read().split()))
    #F = file.read().replace(al, '') 
    '''for i in file.read():
        if i.lower().isalpha():
            continue
        else:
            n += i'''
    m = [re.findall(r'\d+', line) for line in file.readlines()]
    for i in m:
        n += sum(map(int, i))
    
#print(sum(map(int, n.split())))
#print(F)

with open(r'C:\Users\Asus\Desktop\mypy\pytthon\решения\file.txt', 'r') as file:
    '''s = [i for i in file.read().split('\n')]
    file.seek(0)
    let = [i.strip('.,!?;:"\n') for i in file.read().split()]
    file.seek(0)
    l = ''.join([i for i in let])
    print(l)
    print(len(s),len(let), len(l))'''

    text = file.read()
    #print(f"Input file contains:\n{sum(c.isalpha() and c.isascii() for c in text)} letters")
    #print(f"{len(text.split())} words")
    #print(f"{len(text.splitlines())} lines")

#получение путя через getcwd и объединение в путь через джоин    
import os
p = os.path.join(os.getcwd(), 'words.txt')

print(os.path.getsize(p))
all_items = os.listdir()
print(f"Содержимое текущей директории: {all_items}") 

print(os.path.getmtime(p))
print(os.path.exists(p))
print(os.path.isfile(p))
print(os.path.isdir(p))
print(os.path.abspath(p))
print(os.path.dirname(p))
print(os.path.basename(p))
print(os.path.splitext(p))
print(os.path.join(os.getcwd(), 'words.txt'))


with open(p, 'r') as file:
    l = [i for i in file.read().strip().split()] 
    print(*[i for i in l if len(i) == max(list(map(len, l)))],sep='\n')

