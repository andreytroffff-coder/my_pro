n = int(input())
t = []
c1, c2, c3, c4 = 0, 0, 0, 0
for i in range(1,n*2,2):
    num = input()
    t.append(int(num[:num.index(' ')]))
    t.append(int(num[num.index(' '):]))
    x = t[i-1]
    y = t[i]
    if x > 0 and y > 0:
        c1 += 1
    if x < 0 and y > 0:
        c2 += 1 
    if x < 0 and y < 0:
        c3 += 1
    if x > 0 and y < 0:
        c4 += 1
print(f'Первая четверть: {c1} \nВторая четверть: {c2} \nТретья четверть: {c3} \nЧетвертая четверть: {c4}')

'''INPUT
10
17 8
18 8
99 -3
31 -15
11 -41
-1 90
-10 17
-8 15
-84 -9
-10 -3
'''
