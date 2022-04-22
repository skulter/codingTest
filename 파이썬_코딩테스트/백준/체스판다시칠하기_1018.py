n, m = map(int, input().split())
array = []
count = []
for _ in range(n):
    array.append(input())


for i in range(n-7):
    for j in range(m-7):
        wCount = 0
        bCount = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0:
                    if array[x][y] != 'W':
                        bCount += 1
                    if array[x][y] != 'B':
                        wCount += 1
                else:
                    if array[x][y] != 'B':
                        bCount += 1
                    if array[x][y] != 'W':
                        wCount += 1
        count.append(min(wCount, bCount))
print(min(count))
