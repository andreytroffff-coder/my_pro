

'''file = open(r'C:\Users\Asus\Desktop\mypy\pytthon\решения\prices.txt', 'r',encoding='utf-8')
p = 0
for i in file:
    l = i.strip().split()
    p += int(l[-1])*int(l[-2])'''
#print(p)

#________________________________________________________________________________#
#________________________________________________________________________________#


#with open(r'C:\Users\Asus\Desktop\mypy\pytthon\решения\data.txt') as file:
    #for i in file.readlines()[::-1]:
       # print(i.strip())

#________________________________________________________________________________#
#________________________________________________________________________________#

'''with open(r'C:\Users\Asus\Desktop\mypy\pytthon\решения\lines.txt', 'r') as file:
    l = file.read().split('\n')
    mx = len(max(l,key=len))
    for line in l:
        if len(line) == mx:
            print(line)'''

with open(r'C:\Users\Asus\Desktop\mypy\pytthon\решения\nums.txt', 'r',encoding='utf-8') as file:
    for i in file.read():
        print(i)
    




