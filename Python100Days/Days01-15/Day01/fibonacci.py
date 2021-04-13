
def fibonacciNum(num):
    if num == 1:
        return 1
    if num == 2:
        return 1
    if num > 2:
        return fibonacciNum(num-1) + fibonacciNum(num - 2)


for i in range(1, 21):
    print(f'{i}={fibonacciNum(i)}')
    print('\t')
