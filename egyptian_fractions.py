"""Input:
    x :: int
    y :: int
Precondition: 0 < x < y
Output:
    A :: [int]
Postcondition: x/y = sum_i 1/A[i]
"""

def ceiling(x, y):
    if y % x == 0:
        return y // x
    return y // x + 1

def subtract(x, y, n):
    """
    Output integers a,b st a/b = x/y - 1/n
    """
    a = (x * n) - y
    b = y * n
    return a, b

def egyptian_fraction(x, y):
    ###################
    # Your code here! #
    ###################
    if x == 0:
        return []
    greedy = ceiling(x, y)
    x, y = subtract(x, y, greedy)
    return [greedy] + egyptian_fraction(x, y)


print(egyptian_fraction(1, 2))
print(egyptian_fraction(6, 5))
