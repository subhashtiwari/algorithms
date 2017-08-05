# To find a minimum is very easy task, but to remove it is not.

# So the steps are

# 1. Remove the L[0] node.

# 2. copy L[n-1], last node, to L[0] top.

# 3. Run down_heapify(L,0)

# Now write the code to remove the minimum. 

def reomove_min(L):
    L[0] = L.pop()

    down_heapify(L,0)
    return L