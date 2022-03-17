n = input()
result = 0
for m in range(0, len(n)):
    num = int(n[m])
    if m <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)

#예시 답안

# data = input()
# result = int(data[0])
# for m in range(1, len(data)):
#     num = int(data[m])
#     if m <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num
# print(result)