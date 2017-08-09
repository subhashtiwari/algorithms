Running time of Dijkstra in terms of no of nodes n and no of edges m when heaps are used.

These heaps will be able to perform the following functions.

For each node
- Find the shortest distance so far
- remove it, as the operation have been performed on it.
- check each of its neighbour, possibily reducing the distance. As once the value associated with the nodes is reduced, it needs to be some place different in the heap. As the value in the heap is only transferred not eleminated.

The running time for this algorithm is theta(m logn).

As the run time for finding shortest distace takes theta(n logn) time.
And for the edges we do distance reduction operation which also is a theta(mlogn) operation for each edge.

So, by adding these two and assuming that m is at least as big as n and graph is connected. So, m dominates and running time becomes theta(m logn).