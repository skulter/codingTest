import sys

def binary(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        if array[mid] > target:
            end = mid - 1
        if array[mid] < target:
            start = mid + 1
    return -1


M = int(sys.stdin.readline().rstrip())
S = []
for _ in range(M):
    oper = list(sys.stdin.readline().rstrip().split())
    if oper[0] == 'all':
        S = [i for i in range(1, 21)]
        continue
    if oper[0] == 'empty':
        S = []
        continue    
    if len(S) > 0:
        has = binary(sorted(S), int(oper[1]), 0, len(S)-1)
    else:
        has = -1
    if oper[0] == 'add':
        if has == -1:
            S.append(int(oper[1]))
    if oper[0] == 'remove':
        if has != -1:
            S.pop(has)
    if oper[0] == 'check':
        if has != -1:
            print(1)
        else:
            print(0)
    if oper[0] == 'toggle':
        if has != -1:
            S.pop(has)
        else:
            S.append(int(oper[1]))
   
