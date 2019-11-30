# СОРТИРОВКИ

# moduleSORT.py

def inputt(): #ВВОД СПИСКА
    massive = list(map(int, input().split()))
    return massive

def outputt(massive):  #ВВЫВОД СПИСКА
    for i in massive:
        print(i, ' ', end='', sep='')
    print('\n')
    pass


def bubbleSORT(massive):  #ПУЗЫРЁК
    for i in range(len(massive)-1):
        for j in range(len(massive)-1-i):
            if massive[j] > massive[j+1]:
                massive[j], massive[j+1] = massive[j+1], massive[j]
    return massive


def chooseSORT(massive):  #СОРТИРОВКА ВЫБОРОМ
    for i in range(len(massive)-1):
        maximum = 0
        for j in range(1, len(massive)-i):
            if massive[maximum] < massive[j]:
                maximum = j
        massive[maximum], massive[len(massive)-i-1] = massive[len(massive)-i-1], massive[maximum]
    return massive

def quickSort(arr): #БЫСТРАЯ СОРТИРОВКА 
    n = len(arr) 
    if n < 2:
        return arr
    else:
        splitter = arr[0]
        less = [i for i in arr[1:] if i < splitter]
        greater = [i for i in arr[1:] if i > splitter]
        return quickSort(less) + [splitter] + quickSort(greater)    

'''
def insertionSORT(massive):  #СОРТИРОВКА ВСТАВКАМИ
    for i in range(len(massive)-1):
    j=i
    while 0 < j and massive[j] < massive[j-1]:
    j-=1
    massive[j], massive[i] = massive[i], massive[j]
    
    return massive
'''

