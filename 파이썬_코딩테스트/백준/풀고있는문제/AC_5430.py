T = int(input())
for _ in range(T):
    printcount = 1
    oper = input()
    length = int(input())
    arr = input()
    if not length :
        if  oper.count('D'):
            print('error');
            break
        else:
            print('[]')
            break
    arr = list(map(int,arr.replace('[','').replace(']','').split(',')))
    for i in oper:
        if i == 'R':
            arr = arr[::-1]
        if i == 'D':
            if not len(arr) or not length:
                printcount -=1
                print('error')
                break
            arr.pop(0)
    if printcount != 0:
        print('[', end = '')
        for i in range(len(arr)):
            if not i == len(arr)-1 :
                print(str(arr[i])+',' ,end = '')
            else:
                print(arr[i], end = '')
        print(']')
        
        
