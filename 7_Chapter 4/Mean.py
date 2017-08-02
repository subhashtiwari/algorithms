# It is a subroutine mean that will run through all the elements in the list adding up their values. And then returning the total divide by the length.
L = [2, 3, 2, 3, 2, 4]

def mean(L):
    total = 0
    for i in range(len(L)):
        total += L[i]
    return (0.0+total)/len[L]
print mean(L)

# Output is mean = 2.666

# Its running time is theta(n).

# It can be done in a single line though.

print (0.0+sum(L)/len(L))

# But still the running time is theta(n).