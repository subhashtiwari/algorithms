# In this we check the Pairwise Connection, if they are connected or not.

# This code is same as that of the connected component, but we will check here the connection between two nodes only.

def mark_component(G, node, marked):
    marked[node] = True
    total_marked = 1
    for neighbour in G[node]:
        if neighbour not in marked:
            total_marked += mark_component(G, neighbour, marked)
    return total_marked

def check_connection(G,v1,v2):
    marked = {}
    mark_component(G, v1, marked)
    return v2 in marked

print check_connection(G,'a','b')           # The two nodes can be any that are present in the graph. 
                                            # If there is connection between the two nodes then the answer will be true and if not then false.
                                            # Two images named Pairwise 1 & 2 are shown with result.
