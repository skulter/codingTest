import sys
input = sys.stdin.readline
N = int(input())

array = []
for _ in range(N):
    num = 0
    order=(list(input().split()))
    if order[0] == 'push':
        array.append(order[1])
    elif order[0] == 'pop' :
        if  len(array) > 0:
            print(array.pop())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(array))
    elif order[0] == 'empty':
        if len(array) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if len(array) > 0:
            print(array[-1])
        else:
            print(-1)
    