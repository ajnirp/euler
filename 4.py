import sys

max_ = 0
for a in range(1000, 100, -1):
    for b in range(1000, 100, -1):
        prod = a*b
        s = str(a*b)
        if ''.join(reversed(s)) == s:
            max_ = max(max_, prod)

print(max_)