Find the mode : the number that appears the most times.

def mode(L):
    counts = dict()
    maxkey = None
    maxvalue = -1
    for val in L:
        if val not in counts:
            counts[val] = 1
        else:
            counts[val] += 1
        if counts[val] > maxvalue:
            maxkey = val
            maxvalue = counts[val]
    return maxkey
    
    

# The running time for code is theta(n).
 