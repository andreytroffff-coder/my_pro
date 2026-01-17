'''import numpy as np  
# Определение матриц A и B  
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  
B = np.array([[5, 1], [0, 2], [1, 3]])  
# Умножение матриц  
C = np.dot(A, B)  
# Вывод результата  
print(np.linalg.det(A))  '''

'''n1, m1 = map(int, input().split())
ma1 = [list(map(int, input().split())) for _ in range(n1)]
input()
n2, m2 = map(int, input().split())
ma2 = [list(map(int, input().split())) for _ in range(n2)]
if m1 != n2:
    print("Умножение невозможно! Количество столбцов первой матрицы должно равняться количеству строк второй")
else:
    result = [[0 for _ in range(m2)] for _ in range(n1)]
    for i in range(n1):
        for j in range(m2):
            for k in range(m1):  # или range(n2), так как m1 = n2
                result[i][j] += ma1[i][k] * ma2[k][j]
    for i in range(n1):
        for j in range(m2):
            print(result[i][j], end=" ")
        print()'''


'''n1 = int(input())
ma1 = [list(map(int, input().split())) for _ in range(n1)]  # исправлена синтаксическая ошибка
n = int(input())

# Инициализируем результат как единичную матрицу (для степени 0)
result = [[1 if i == j else 0 for j in range(n1)] for i in range(n1)]

# Возводим матрицу в степень n
for _ in range(n):
    temp = [[0 for _ in range(n1)] for _ in range(n1)]
    for i in range(n1):
        for j in range(n1):
            for k in range(n1):
                temp[i][j] += result[i][k] * ma1[k][j]
    result = temp'''

# Вывод результата
'''for i in range(n1):
    for j in range(n1):
        print(result[i][j], end=" ")
    print()'''


#Функция zip() используется для совмещения двух и более списков в один. 
#Она возвращает итератор кортежей, где i-ый кортеж содержит i-ый элемент из каждого из переданных списков.

x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print(list(zipped)) 
# Выведет: [(1, 4), (2, 5), (3, 6)]
#Также функция zip() может быть использована для «расстегивания» списка кортежей обратно в отдельные списки. 
#Для этого используется оператор «*». Он позволяет преобразовать список в набор аргументов для функции.

zipped = [(1, 4), (2, 5), (3, 6)]
x, y = zip(*zipped)
print(list(x)) 
# Выведет: [1, 2, 3]
print(list(y)) 
# Выведет: [4, 5, 6]

def transpose_matrix(matrix):
    '''n = len(matrix)      # количество строк
    m = len(matrix[0])   # количество столбцов
    
    # Создаем новую матрицу с обратными размерами m x n
    transposed = [[0] * n for _ in range(m)]
    
    # Заполняем транспонированную матрицу
    for i in range(n):
        for j in range(m):
            transposed[j][i] = matrix[i][j]'''
  
    return [list(row) for row in zip(*matrix)]
#print(transpose_matrix())
import numpy as np
m = np.array([[1,2,3],[4,5,6],[7,8,9]])
for i in m:
    print(*i)
print(m.swapaxes(0,1))
print(m.transpose())
print(m.T)
print(m.T[0])
 
