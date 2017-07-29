# For a recursively generated graph if the template says that if we want one node, it'll just return a single node. 
# For other values, make a G1 and G2 that are half the size. And then we make log n connection between G1 and G2 by picking a random point and connecting with a random node.  
# Another random node with another random node etc. And, then return. 
# So, this has the recurrence relationship that is T(1) = 0 i.e. zero edges for one node.
# For n nodes we get 2 times the number of nodes we have for a graph of half the size plus big theta of log n. i.e. T(n) = 2T(n/2) + theta(log(n))


def makeG(N):
    if n == 1:
        return <a single node>
    g1 = makeG(n / 2)
    g2 = makeG(n / 2)
    for i in range(log(n))
        i1 = <random node from g1 without replacement>
        i2 = <random node from g2 without replacement>
        make_link(g, i1, i2)
    return G

# Solve the recurrence relation.

# For this code T(n) = theta(n log(n))

# As for first level (n) : log(n)
# Second level (n/2) : log(n/2) + log(n/2) = 2 log(n) - 2
# Third Level (n/4) : 4 log(n) - 4

# n level (n/n) : n log(n) - n
# Adding all levels...
# (n log(n) - n) + (n/2 log(n) - n/2) + (n/4 log(n) - n/4)+ ... + log(n) = 2n log(n) - 2n = theta (n log(n))
# So T(n) = theta n(log(n))