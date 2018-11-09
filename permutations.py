# ВСЕВОЗМОЖНЫЕ ПЕРЕСТАНОВКИ ЧИСЕЛ ЧЕРЕЗ РЕКУРСИЮ

def inputt(): # ВВОД МАССИВА ЧИСЕЛ
    massive = list(map(int, input().split()))
    return massive

def outputt(massive): # ВЫВОД 
    for i in massive:
        print(i, '  ', end='')
    print('\n')
    pass

def permutations(massive, begin): # РЕКУРСИОННАЯ ФУНКЦИЯ ФИКСИРУЩАЯ 1 ЭЛЕМЕНТ, ПОКА НЕ ДОЙДЕТ ДО ПОСЛЕДНЕГО
    if begin == len(massive):     
        outputt(massive)
    else:
        for i in range(begin, len(massive)):
            massive[begin], massive[i] = massive[i], massive[begin]
            permutations(massive, begin+1)
    pass

def main():
    permutations(inputt(), 0)

main()
