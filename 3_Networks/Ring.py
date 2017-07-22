def make link(G, node1, node2):
    if node1 not in G:
        G(node1) = {}
    (G[node1])(node2) = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])(node1) = 1
    return G


# Make an empty graph
a_ring = {}

n = 5

# Add in the edges
for i in range (n):
    make_link(a_ring, i, (i+1)%n)

# How many nodes?
print len(a_ring)

# How many edges?
print sum([len(a_ring[node])for node in a_ring.keys()])/2       # It gives us a list of the degrees of all teh nodes, sum all these and divide 
                                                                # by two as we've counted each edge twice. So we get the number of edges.
print a_ring


# We're making a graph and call it a_ring. Set it equal to 5 and intialize the ring to be an empty dictionary.
# In this we're going to add edges in this empty graph.
# The particular edges that we add  are in a loop from 0 to n-1.
# We make a link in the ring from node i to node i+1 mod n. It will wrap around at the very end.
# make_link takes a graph or a dictionary and two nodes if we want to connect together, checks whether the first node is already in the graph.
# If it is not, then it creates an empty dictionary for that node. Same for node2.
# Then it goes to the dictionary for node1 in the graph and says that there is a connection to node 2.
# It basically connects node1 & node2 so it can be checked when required.

# The no of nodes is 5
# The no of edges is 5. 