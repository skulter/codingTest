# N = int(input())
# K = int(input())
# isVisit = [False] * (N + 1)
# isVisit[0] = True
# queue = []
# queue.append([] )
# for _ in range(K):
#     queue.append(list(map(int,input().split())))

# for node in queue:
#     if isVisit[node[0]-1] or isVisit[node[1]-1]:
#         isVisit[node[1]-1] = True
#         isVisit[node[0]-1] = True
# print(isVisit.count(True)-1)


# dfs
N = int(input())
K = int(input())
isVisit = [False] * (N + 1)
graph = [[] for _ in range(N+1)]
for _ in range(K):
    x, y = list(map(int, input().split()))
    graph[x].append(y)
    graph[y].append(x)


def dfs(graph, x, isVisit):
    isVisit[x] = True
    for i in graph[x]:
        if not isVisit[i]:
            dfs(graph, i, isVisit)
dfs(graph, 1, isVisit)
print(isVisit.count(True)-1)
