from collections import deque
import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
q = deque([])
graph = []
# graph = [list(map(int, input().split())) for _ in range(M*H)]

# for z in range(H):
#     for x in range(N):
#         for y in range(M):
#             if graph[z][x][y] == 1:
#                 q.append((z, x, y))

def flatten(lst):
    result = []
    for item in lst:
        if type(item) == list:
            result += flatten(item)
        else:
            result += [item]
    return result

for z in range(H):
    tmp = []
    for y in range(M):
        tmp.append(list(map(int, input().split())))
        for x in range(N):
            if tmp[y][x] == 1:
                q.append([z, y, x])
    graph.append(tmp)

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while q:
    z, y, x = q.popleft()

    for i in range(6):
        nx = x+dx[i]
        ny = y+dy[i]
        nz = z+dz[i]
        if 0 <= ny < M and 0 <= nx < N and 0 <= nz < H and graph[nz][ny][nx] == 0:
            q.append((nz, ny, nx))
            graph[nz][ny][nx] = graph[z][y][x] + 1

graph = flatten(graph)

if graph.count(0):
    print(-1)
else:
    print(max(graph)-1)