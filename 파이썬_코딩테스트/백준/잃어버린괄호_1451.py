exp = input().split('-')

sumNum = []
plus =[]
result = 0
for i in exp:
    plus.append(i.split('+'))
for j in plus:
    if len(j) > 1:
        sumNum.append(sum(map(int,j)))
    else:
        sumNum.extend(list(map(int,j)))

initNum = sumNum[0]
for i in range(1,len(sumNum)):
    initNum -= sumNum[i]
print(initNum)