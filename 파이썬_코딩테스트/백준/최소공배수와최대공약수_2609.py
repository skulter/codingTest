n, m = map(int, input().split())


def gcd(n, m):
    remain = n % m
    if remain != 0:
        return gcd(m, remain)
    else:
        return m


gcdValue = gcd(n, m)


def lcm(n, m):
    return int(n * m / gcdValue)


print(gcdValue)
print(lcm(n, m))
