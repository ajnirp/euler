a, b, sum_ = 1, 2, 0
while b < 4e6:
    sum_ += b
    # shift the window thrice so that once more we have a odd, b even
    # this ensures we get all the even numbers
    for _ in range(3):
        a, b = b, a + b
print(sum_)