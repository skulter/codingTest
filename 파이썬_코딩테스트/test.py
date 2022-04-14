N = int(input())

array = []
array_set = {}

for _ in range(N):
    array.append(input())

array_set = set(array)
array = list(array_set)

print(array)
array.sort(key = len)
print(array)

array.sort()
print(array)

# for i in array:
#     print(i)
