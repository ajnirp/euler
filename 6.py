def sum_of_squares(n):
    return n*(n+1)*(2*n+1) // 6

def square_of_sum(n):
    sum_ = n*(n+1) // 2
    return sum_*sum_

print(abs(sum_of_squares(100) - square_of_sum(100)))