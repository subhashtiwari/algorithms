# What is the average value of C(w,x) if we choose a random node v from graph.
# And then choose a pair of neighbour of that particular chosen node v randomly from graph.
# And then return either 1 or 0 depending whether those two nodes are connected or not. 

# The average is over two sources of randomness that we're randomizing overall nodes and overall pairs.

# The expected value of some random variable x is the sum of all values that the variable can take on, the value of thet variable times the probability.

# Write the code for finding the expected value of C(w,x).

def expected_C(G,v):
    return clustering_coefficient(G,v)

# The answer to this code is actually the clustering coefficient code as it returns the approximated value for any node.
# The value will be 1 at the starting but as the code repeats the value will flucuate around 0.3, i.e. it can be 0.27, 0.29, 0.31 etc.
# The value converges to actual clustering coefficient. 

def clustering_coefficient(G,v):
    neighbours = G[v].keys()
    degree = len(neighbours)
    if len(neighbours) == 1: return 0.0
    links = 0.0
    for w in neighbours:
        for u in neighbours:
            if u in G[w]: links += 0.5
    return 2.0*links/(len(neighbours)*(len(neighbours)-1))

v = 2                                       # It can be the number of the node we want Clustering Coefficient of
print "CC:", clustering_coefficient(G,v)

# To choose different neighbours randomly move them into an array vindex.
# By this we choose indices from this array and thus they don't repeat.
vindex = {}
d = 0                   
for w in G[v].keys():
    vindex[d] = w
    d += 1                      

total = 0
for i in range(1,1000):
    if d > 1:                                                # d is the degree of node v. And as log as it is greater than 1 we can pick a random neighbour.
        pick = random.randint(0,d-1)                         # Neighbour is chosen by its ordering from 0 to d-1.
        v1 = vindex[pick]                                    # v1 is the neighbour- the actual name associated with that pick. 
        v2 = vindex[(pick+random.randint(1,d-1))%d]          # v2 is the second pick that will choose from 1 to d-1. Add this to the pick that we already got with modular d to make it wrap aroud. This make sure we pick a different node than the earlier one.
        if v2 in G[v1]: total +=1                            # if they are connected then we add 1 to the total.
    print i, (total+0.0)/i                                   # Repeat this loop thousand times and each time take the total number of things that are connected divided by the total number of times we tried.


# Thus the actual number converges to the actual clustering coefficient.