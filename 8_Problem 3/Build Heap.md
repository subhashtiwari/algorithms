Another way to build a heap out of a set of values, is to insert the items one at a time into heap.

The code:
##
heap = []
for v in vals:
    insert_heap(heap,v)        
##
# Insert heap is : def insert_heap(L, v): L.append(v) up_heapify(L, len(L)-1)


What is the runnnig time of this code?
theta(n logn) : As it will first insert elements then travers up to check if the numbers are inserted correctly. 
