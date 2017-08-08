# In this we give it a single node in the network and then ask for the distance to all other nodes in the network in graph G.

def dijkstra(G,v):
    dist_so_far = {}                    # This structure represents a mapping from nodes to the distance from V to that node.
    dist_so_far[v] = 0                  # Distance from v to v i.e. zero.
    final_dist = {}                     # In this structure we figure out the real distance is.
    while len(final_dist) < len(G):
        w = shortest_dist_node(dist_so_far)
        print "lock", w, dist_so_far[w]
        final_dist[w] = dist_so_far[w]
        del dist_so_far[w]
        for x in G[w]:                  # In here we get a node that is w in here and find the distance of all its neighbours.
            if x not in final_dist:
                if x not in dist_so_far:
                    dist_so_far[x] = final_dist[w] + G[w][x]            # In this we check if the node has no dist then we give it the distance by that formula.
                elif final_dist[w] + G[w][x] < dist_so_far[x]:          # In case it already have a distance then check if the new distance, the distance to w plus the distance from w to x, is better than the distance that we had so far and if it is then replace it.
                    dist_so_far[x] = final_dist[w] + G[w][x]                
                                                                        # After w node we check the next node and its neighbours and run the same method again for each one.
return final_dist                                                       # When all the assigning is done we return the structure. 
                    
print dijkstra(G, a)


# The running time of Dijkstra depends on how find shortest is implemented.