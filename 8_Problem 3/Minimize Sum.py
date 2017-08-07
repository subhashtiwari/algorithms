# Minimize Sum of Absolute Value 

# Given a list of numbers, L, find a number, x, that minimizes the sum of the absolute value of the difference
# between each element in L and x : SUM_{i=0}^{n-1} |L[i] -x|

# Runnig time should be theta(n)


def minimize_absolute(L):
    x = 0
    return avg(L)

# So x should be equal to the average of the items on the list.

# Such as if there are 6 items then x = sum of (all six numbers)/6.