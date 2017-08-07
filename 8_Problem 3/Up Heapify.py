# write up_heapify, an algorithm that checks if
# node i and its parent satisfy the heap
# property, swapping and recursing if they don't
#
# L should be a heap when up_heapify is done.

def up_heapify(L,i):
  while  L[i] < L[parent(i)] and i > 0
         (L[parent(i)],L[i]) = (L[i],L[parent(i)])
         i = parent(i)

         
