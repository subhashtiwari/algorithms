Floyd-Warshall 

It is helpful in case for finding the shortest path in a Dense Graph with less running time.
It uses an idea called dynamic programming. It is an algorithm design technique.
It doesn't change the way you think about programming. It just have to do with optimizing using tables. 

To understand it better 
Assume, all nodes in our graph are numbered from 0 to n-1. And all our characters be assigned from 0 to n-1. 
Assume that there is a square matrix D of k and the entries of this matrix, just like a spread sheet is filled in with values as follows:

The ij element of i row, j column is filled in with a number, and that number is the length of the shortest path from i to j, hopping only all nodes numbered less than k.

Assume that we've got a graph and we're tryin  to get  a path from i to j and some of the nodes are okay nodes because they are numbered less tahnn k and some nodes, maybe including j itself are numbered higher than k, and we're not allowed to step on those. 

We want to know the distance of the shortest path using only the pink nodes, only that are numbered less than k.

And the D to k matrix is already filled with these values and now we find out Dk+1 matrix, where we can use the node k when we're going on a path from i to j.

So, now we've to find Dk+1 when Dk is already given.

There are tow possibilities. 
1. Maybe we don't need to use k at all for the smallest path, we follow path fro i to j only using nodes who have values less than k.

2. Or we go and visit k and then go from k to j. But in visiting k, we don't ever need to visit k on the way to k that wouldn't be a very good path. 

So, the shortest path from i to k only using the nodes that are less than k, then wefollow another path now from k to j only using nodes whose number are less than k.
The only thing that could happen is we don't visit k twice and we're not allowed to use any nodes that are greater than k. 

So of these two possibilities whichever one is shortest, the direct path from i to j or the linked path from i to j through k, is the shortest path from i to j possibly using k. 

So, as we already have the shortest path from i to j without using k. We only need to find the other one.

To find this follow the steps:

1. For all i, j : D^0[i][j] = cost[i][j]         
# Length of the shortest path from i to j using nodes only numbered less than zero. It is equal to the direct cost from going i to j. 

2. For k from 0 to n-1:     
# Run k from 0 to n-1. This loop run over all pairs of nodes i.i n^2, but it also runs from 0 to n-1 for each value so its n^3.
3. For all i j : D^k+1[i,j] = m.n(D^k[i,j], D^k[i,k] + D^k[k,j])
# Add the path from i to j is the sum of path from i to k and k to j

4. return D^n
# D^n[i,j] is the length of shortest path from i to j using nodes numbered less than n, this takes all of the nodes as the nodes are numbered 0 to n-1.


The running time of this algorithm is theta(n^3) which is better than theta(n^3 logn) for repeated Dijkstra for a Dense Graph. 