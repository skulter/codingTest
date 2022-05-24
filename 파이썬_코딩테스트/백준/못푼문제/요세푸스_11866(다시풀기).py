# # N, K = map(int, input().split())

# N = int(7)
# K = int(3)
# array = []
# answer = []
# for i in range(N):
#     array.append(i+1)

# count = 1
# while array:
#     if (K * count) - 1 <= len(array):
#         answer.append(array[(K * count) - 1])
#     else:
#         K -= 1
#         count = 1
#     count += 1
# print(answer)


n, k = map(int, input().split()) 

people = [i for i in range(1, n+1)] 
key = 0
temp = k - 1 
order = [] 
while people: 
    key = (key+temp) % len(people)
    order.append(people.pop(key)) 
print('<'+', '.join(map(str, order))+'>')

