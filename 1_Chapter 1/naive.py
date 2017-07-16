def naive(a, b):
    x = a; y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z


#This code takes two non zero inputs and runs for sometime and then it returns z.

#What this code is doing is basicially multiplication of a with b
#Or whatever value you use for input of x and y.

# ab=xy+z
# when x = 0    xy + z = ab, becomes
#               0y + z = ab so we get z = ab.

# In the code each time it goes through, it is decrementing x accounting the values in z and eventually when x is null, it returns z and it is exactly a times b.

# The running time of the code is roughly linear.