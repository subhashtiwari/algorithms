# Write code to find the maximum value  in L 


def max(L):
    max_so_far = L[0]
    for i in range(1,len(L)):
        if L[i] > max_so_far: max_so_far = L[i]
    return max_so_far

print max(L)