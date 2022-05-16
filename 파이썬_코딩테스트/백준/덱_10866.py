import sys
input = sys.stdin.readline

N = int(input())
deque = []
for _ in range(N):
    oper = list(input().split())
    if oper[0] == 'push_front':
        deque.insert(0, oper[1])
    if oper[0] == 'push_back':
        deque.append(oper[1])
    if oper[0] == 'pop_front':
        if len(deque) > 0:
            print(deque.pop(0))
        else:
            print(-1)
    if oper[0] == 'pop_back':
        if len(deque) > 0:
            print(deque.pop())
        else:
            print(-1)
    if oper[0] == 'size':
        print(len(deque))
    if oper[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    if oper[0] == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    if oper[0] == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])