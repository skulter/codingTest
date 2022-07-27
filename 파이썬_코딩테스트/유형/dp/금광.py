# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N = int(input())

tree = []
answer = 0
for _ in range(N * 2 -1):
	tree.append(list(map(int,input().split())))

def dfs():
    for i in range(N**2):
        pass

print(max(tree[0])+1)