import sys
input = sys.stdin.readline
n, m = map(int, input().split())
pokets = dict()

for i in range(1, n+1):
    pokets[i] = input().rstrip()

poket_revers = dict(map(reversed, pokets.items()))
for i in range(m):
    search = input().rstrip()
    if search.isdigit():
        print(pokets[int(search)])
    else:
        print(poket_revers[search])
