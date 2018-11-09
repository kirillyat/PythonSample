# СОРТИРОВКИ

# moduleSORT.py

def inputt():
    massive = list(map(int, input().split()))
    return massive

def outputt(massive):
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

'''
    def insertionSORT(massive):  #СОРТИРОВКА ВСТАВКАМИ
    for i in range(len(massive)-1):
    j=i
    while 0 < j and massive[j] < massive[j-1]:
    j-=1
    massive[j], massive[i] = massive[i], massive[j]
    
    return massive
    '''


def main():
    outputt(insertionSORT((inputt())))
    
    pass

main()
