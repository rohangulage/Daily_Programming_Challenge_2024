import math

def lcm(N, M):
    return abs(N * M) // math.gcd(N, M)

N = 12
M = 18
print(lcm(N, M))
