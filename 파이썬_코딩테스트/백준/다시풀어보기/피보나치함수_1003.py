N = int(input())
do = [0] * 41
dz = [0] * 41
do[0], do[1] = 1, 0
dz[1], dz[0] = 1, 0


for i in range(2, 41):
    do[i] = do[i-1] + do[i-2]
    dz[i] = dz[i-1] + dz[i-2]

for _ in range(N):
    v = int(input())
    print(do[v], dz[v])
