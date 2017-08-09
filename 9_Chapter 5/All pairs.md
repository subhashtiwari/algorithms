All pairs shortest paths

As we know that, to find the most central node we find the shortest distance of a node from all the other nodes in a graph, to get a square for a particular node.
And then repeat that operation to find out the distance from every other node to every other node.
So, actually finding the shortest distance between any pair of nodes.

As Dijkstra take theta(m logn) to find a shortest path from any given node.
For All Pairs we can run the Dijksra for each node thus running time would become theta(nm logn). As it repeats for all the nodes.

If the graph is sparse then n and m are compareable and it becomes theta(n^2 logn).

If the graph is densely connected then the number of edges is roughly the square of the number of nodes so the runnnig time becomes theta(n^3 logn).