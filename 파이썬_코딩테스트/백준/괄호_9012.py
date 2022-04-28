N = int(input())

for _ in range(N):
    array = []
    word = list(input())
    answer = 'NO'

    for i in range(len(word)):
        if word[i] == '(':
            array.append(word[i])
        if word[i] == ')':
            if len(array) >= 1:
                array.pop()
            else:
                array.append(word[i])
                break
    if len(array) >= 1:
        print('NO')
    else:
        print('YES')
