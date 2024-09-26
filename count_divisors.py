def count_divisors(N):
    count = 0
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            if i == N // i:
                count += 1
            else:
                count += 2
    return count

N = 100
print(f"Total number of divisors of {N} is {count_divisors(N)}")
