import numpy as np # Импорт библиотеки

n = 10

Z = np.zeros(n) # Массив-вектор из n нулей
print(Z)

Z = np.ones(n) # Массив-вектор из n единиц
print(Z)

Z = np.full(n, 3.1415) # Массив-вектор из n чисел
print(Z)

Z = np.array([1, 2, 3]) # Массив в NP из масива python
print(Z)

Z = np.ones(n)
Z[1] = 25 # Изменение 1 элемента
print(Z)

Z = np.arange(n)  # Создание массива из n элементов 0,1...n
# Z = np.full(n,range(n))
print(Z)

Z = Z[::-1] # реверс массива
print(Z)
