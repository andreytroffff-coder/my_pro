#прога для вычисления кубов
print(*[int(i)**3 for i in input().split()])

#выаодит слова из строки
print(*[i for i in input().split()],sep='\n')

#вывод четных чисел больше 2
print([i for i in range(2,int(input())+1,2)])

#нахождение самого длинного слова из списка
print(max([len(i) for i in input().split()]))

#количество уникальных значений
n = [int(i) for i in input().split()]
print(len(set(n)))

#количество решек в комбинации
print(len(max([i for i in input().split('О')])))

#Количество объединенных 
print(len(set(input().split()) & set(input().split())))