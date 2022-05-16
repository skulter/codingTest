N = int(input())

def fectorial(x):
    if x == 1:
        return 1
    return x * fectorial(x -1) 



if N == 0 :
    print(0)
else:
    cnt = 0
    v = str(fectorial(N))
    for i in v[::-1]:
        if int(i) == 0:
            cnt += 1
        else:
            break

    print(cnt)
