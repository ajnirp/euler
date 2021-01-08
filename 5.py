# euclidean algorithm
def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if 1 in [a, b]:
        return 1
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

# assumes n > 3
# lcm(a, b, c) = lcm(lcm(a, b), c)
def lcm_upto(n):
    ans = 2 # lcm(1, 2)
    for i in range(3, n):
        ans = lcm(ans, i)
    return ans

print(lcm_upto(20))