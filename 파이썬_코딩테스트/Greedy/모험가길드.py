n = input()
data = list(map(int, input().split()))
data2 = data
data.sort(reverse=True)


start = 0


for i in data:
    if i == n:
        start += 1
        break
    if len(data) == 0:
        break
    data = data[i:]
    start += 1

print(start)
