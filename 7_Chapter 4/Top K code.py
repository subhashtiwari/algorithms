# This algorithm runs top K algorithm.

# This algorithm builds a list for us, it actually seperates that into three pieces, the ones that are smaller than v, the v and the ones that are bigger than v.
def partition(L, v):
    smaller  = []
    bigger = []
    for val in L:
        if val < v: smaller += [val]
        if val > v: bigger += [val]
    return (smaller, [v], bigger)


# This algorithm takes a list and some number K that we want that the smallest K elements of L.
# It do a partition of L on v and seperates it into the left, the middle, and the right.
# If the size of the thing on the left is exactly K, we're done. The thing on the left is what reqiured.
def top_k(L, k):
    v = L[random.ranrange(len(L))]
    (left,middle,right) = partition(L,v)
    if len(left) == k: return left
    if len(left)+1 == k: return left+[v]                # If the length of the thing onthe left plus 1 is equal to K then we still got the answer as it's on the left side including v.
    if len(left) > k: return top_k(left, k)             # But when the stuff on the left is bigger than K, we get more than the top K.
    return left+[v]+top_k(right,k-len(left)-1)

print top_k(L,5)


# So, it gives out the exactly five smallest elements of L, but not sorted though.