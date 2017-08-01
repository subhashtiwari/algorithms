# This algorithm returns the maximum distance from a node to all other nodes it can reach.

def centrality_max(G, v):
    distance_from_start = {}
    open_list = [v]
    distance_from_start[v] = 0
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + 1
                open_list.append(neighbor)
    return max(distance_from_start.values())


# We go to open list, pull the first element off at the current node that we were working on, pop it off the list.
# Then in the for loop we look at the neighbours of that node. If this neighbour is a new neighbour, then we make a note of it's distance which is distance from the start to the node we just were plus one to get the distance to the neighbour then we put it on the open list.
# Once the open list is exhausted, we visited all the nodes that were reachable and put their distances from the start state into the data structure : distance from the start.
# In the return statement we get the maximum distance.