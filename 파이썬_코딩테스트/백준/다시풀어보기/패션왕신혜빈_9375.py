# n = int(input())


# def fectorial(x):
#     if x <= 1:
#         return 1
#     return x * fectorial(x-1)


# def p(n, r):
#     return fectorial(n) // fectorial(n-r)

# def c(n, r):
#     return fectorial(n) // fectorial(n-r) * fectorial(r)

# def valueSum(i):
#     sum = 0
#     for j in i:
#         sum += close[j]
#     return sum


# for _ in range(n):
#     k = int(input())
#     close = dict()
#     for _ in range(k):
#         name, kind = input().split()
#         if close.get(kind) == None:
#             close[kind] = 1
#         else:
#             close[kind] += 1
#     sum = 0
#     value = valueSum(close)
#     for i in range(1, value):
#         sum+= p(i, value)
#     print(sum-1 + k)


# # def c(n, r):
# #     print(fectorial(n) // fectorial(n-r) * fectorial(r))


# # print(p(2, 3), c(2, 2))


n = int(input())

for _ in range(n):
    k = int(input())
    wear = dict()
    sum = 1
    for _ in range(k):
        name, kind = input().split()
        if wear.get(kind) == None:
            wear[kind] = 1
        else:
            wear[kind] += 1
    for k in wear:
        sum *= (wear[k] + 1)
    print(sum-1)