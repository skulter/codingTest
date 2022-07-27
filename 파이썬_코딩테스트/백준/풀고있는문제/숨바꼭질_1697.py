from collections import deque

N, K = map(int, input().split())
dist = [0] * 100001
move = [0] * 100001


def bfs():
    q = deque([N])

    while q:
        val = q.popleft()
        if val == K:
            print(dist[val])
            path(val)
            return
        for i in (val-1, val+1, val * 2):
            if 0 <= i <= 100000 and not dist[i]:
                q.append(i)
                dist[i] = dist[val] + 1
                move[i] = val


def path(x):
    arr = []
    for _ in range(dist[x]+1):
        arr.append(x)
        x = move[x]
    print(' '.join(map(str, arr[::-1])))


bfs()
