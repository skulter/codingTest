import sys
taseCaseCount = int(input())

for _ in range(taseCaseCount):
    n, m = map(int,input().split())
    importanceArr = list(map(int,input().split()))
    targetArr = [0] * n
    targetArr[m] = 1
    count = 0
    
    while True:
        if importanceArr[0] == max(importanceArr):
             count += 1
             if targetArr[0] == 1:
                print(count)
                break
             else:
                 del importanceArr[0]
                 del targetArr[0]
        else:
             importanceArr.append(importanceArr[0])
             targetArr.append(targetArr[0])
             del importanceArr[0]
             del targetArr[0]

