
def fectorial(x):
    if x <= 1:
        return 1
    return x * fectorial(x-1)

print(fectorial(int(input())))