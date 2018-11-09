#ПЕРЕСТАНОВКИ ЧИСЕЛ

def inputt():
    massive = list(map(int, input().split()))
    return massive

def outputt(massive):
    for i in massive:
        print(i, '  ', end='')
    print('\n')
    pass

def permutations(massive, begin):
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