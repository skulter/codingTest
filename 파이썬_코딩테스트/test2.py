# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
intervalList = [False] * 20000
for i in range(n):
    interval = list(map(int, input().split()))
    count = int(interval[0])
    for i in range(count):
        start, end = interval[i+1:i+3:]
        print(start, end)

print(intervalList)