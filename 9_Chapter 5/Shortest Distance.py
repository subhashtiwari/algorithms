# In this we find the smallest value and then delete it from the set of Dijkstra Algorithm. 
# So that we don't get the same value over and over again.
# There can be at most one for each node then less.
# To get the smallest distance, loop through the list. Take all the distances that are present and just loop through them and pull out the minimum, it takes theta(n) time.


def shortest_dist_node(dist):
    best_node = 'undefined'
    best_value = 1000000
    for v in dist:
        if dist[v] < best_value:                        # If the distance for that node is better than the best we've seen so far, reassign and return the best node.
            (best_node, best_value) = (v, dist[v])
    return best_node


# The running time of Dijkstra with this implementation for this is theta(n^2).
# As for each node in Dijkstra we do following operations
# Find the shortest dist_so_far
# Remove it
# Check for its neighbours.
# With all this it takes around theta(n^2) as the number of edges are around 0 to n^2 so 2n^2 so theta(n^2).


# As it is a longer running time we will try doing this by heap with shorter running time.
