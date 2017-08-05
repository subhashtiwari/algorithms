# In this we write a code to get a correct heap. 
# Given a position i in the heap, left 'i' returns the position of teh left child. Right 'i' return the position of right child. Parent 'i' returns the position of the parent.
# Rooot of 'i' answers whether or not the node in question is a root. 
# Leaf (L, i) returns whether or not we're looking at a leaf 'i'. In other words, it has no children, it has no children if what where the right child would be is off the end of teh list and where the left child would be is off the end of the list. 
# One child node :  if a node has only one child, which is the very last element in the array. SO, the other child doesn't exist. 


L = [50, 88,27, 58, 30, 21, 58, 13, 84, 25, 29, 43, 61, 44, 65, 74, 76, 30, 82, 42]

def left(i): return i*2+1
def right(i): return i*2+2
def parent(i): return (i-1)/2
def root(i): return i==0
def leaf(L, i): return right(i) >= len(L) and left(i) >= len(L)
def one_child(L, i): return right(i) == len(L)

def down_heapify(L, i):
    if leaf(L, i): return                               # If i is a leaf

    if one_child(L, i):                                 # If i has one child
        if L(i) > L[left(i)]:
            (L[i], L[left(i)]) = (L[left(i)], L[i])
            return

    if min(L[left(i)], L[right(i)]) >= L[i]: return     # If i has two children

    if L[left(i)] < L[right(i)]:
        (L[i], L[left(i)]) = (L[left(i)], L[i])

    down_heapify(L,left(i))
    return
    (L[i], L[right(i)]) = (L[right(i)], L[i])
    down_heapify(L,right(i))
    return



# This routine is called if the heap rooted at i satisfies the heap property
# except perhaps i to its immediate children

# The running time of this code is theta(logn). As it is a tree. 