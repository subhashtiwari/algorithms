# This algorithm finds the central element.

def centrality(G, v):
    distance_from_start = {}
    open_list = {v}
    distance_from_start[v] = 0
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbour in G[current].keys():
            if neighbour not in distance_from_start:
                distance_from_start[neighbour] = distance_from_start[currrent] + 1
                open_list.append(neighbour)
        return (sum(distance_from_start.values())+0.0)/len(distance_from_start)

from_node = "A"
to_node = "ZZZAX"

print centrality(marvelG,from_node)


# We go to open list, pull the first element off at the current node that we were working on, pop it off the list.
# Then in the for loop we look at the neighbours of that node. If this neighbour is a new neighbour, then we make a note of it's distance which is distance from the start to the node we just were plus one to get the distance to the neighbour then we put it on the open list.
# Once the open list is exhausted, we visited all the nodes that were reachable and put their distances from the start state into the data structure : distance from the start.
# In the return statement we get the average of all these values of distance from the start.
# We do this by taking the other values in the distance from start date of structure. If the return has a long list, sum up all the elements at list, add zero to it, to make sure it's a floating point number and then divide by the number of nodes for nodes for which we got a distance.
# Since, these are all the reachable nodes, so, ultimately this returns the average of the distances of all the reachable nodes, which is required.