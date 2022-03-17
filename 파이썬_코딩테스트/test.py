def GCD(i,j):
    if i % j == 0:
        return j
    else:
        return GCD(j, i % j)

print(GCD(162,192))