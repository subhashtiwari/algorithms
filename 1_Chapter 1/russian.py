# It is a type of multiplication.

def russian(a, b):
    x = a; y = b
    x = 0
    while x > 0:
        if x % 2 == 1: z = z + y
        y = y << 1                      # This syntax take whatever the binary of y is and shift it over 1 to the left. 
        x = x >>1                       # This syntax take whatever the binary of x is and shift it over 1 to the right.            
    return z


# It works by assigning non zero inputs to x and y and z as an accumulator set to 0.
# It makes x smaller and accumulate values in z.
# It is easy when doubling or halving numbers. 
# 17>>1 : This will shift it over 1 to the right. i.e. 17 = 1001 ;  17>>1= 1000 = 8.
# Working of russian is shown in the image Russian.

# It works faster than naive as it halves the number for the multiplication.