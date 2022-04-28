N = int(input())

array = []
rankList = []
for _ in range(N):
    weight, height = map(int, input().split())
    array.append((weight, height))

for i in array:
    rank = 1
    for j in array:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')

