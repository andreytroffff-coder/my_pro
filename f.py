with open(r'C:\Users\Asus\Desktop\mypy\pytthon\решения\logfile.txt', 'r', encoding='utf-8') as lg, open('output.txt', 'w', encoding='utf-8') as out:
    for line in lg.readlines():
        l = line.split(',')
        tim = list(map(int, l[1].split(':') + l[-1].split(':')))
        if (tim[2] - tim[0]) * 60 + (tim[-1] - tim[1]) >= 60:
            out.write(l[0] + '\n')
