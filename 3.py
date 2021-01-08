from math import sqrt

def is_prime(n):
    high = int(sqrt(n))
    # decrement high if it's even
    if high & 1 == 0:
        high -= 1
    i = high
    while i > 0:
        if n % i == 0:
            break
        i -= 2
    return i == 1

def largest_prime_factor(n):
    high = int(sqrt(n))
    # decrement high if it's even
    if high & 1 == 0:
        high -= 1
    for i in range(high, 1, -2):
        if n % i == 0 and is_prime(i):
            return i
    return n

print(largest_prime_factor(600851475143))