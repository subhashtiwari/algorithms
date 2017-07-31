Now we will find the shortest path from a single node V1 to all other nodes. Instead of finding shortest path betweeen two nodes.
We do this to find the central node in a social network.
Nodes that are likely to have a lot of influnce, or well-placed, or very well-connected so we will find how central the node in question V1 is.

There are many different ways that can define what central means.
For now we find the average shortest path length to all the other nodes. So, we calculate the shortest path length from V1 to all other nodes. 

As we know shortest path length V1 to V2 takes this much time : theta(m+n), where m is no of edges and n is no of nodes.
So, to find shortest path for all the possible target nodes we should repeat this for all nodes : theta (n(n+m)).
So, we find the shortest path from V1 to V2 and from V1 to V3 and V1 to V3 till the last connecting nodes. Then get all the distances and then average them to get this measure of centrality.
The running time for that approach is going to be big theta (n), the number of nodes times the time that it takes to do a shortest path search.
So, it's really n times n plus m which is (n^2 + nm).
But in real world scenerio we will have no of nodes that can go up to 5000 and 5000^2 will be a big no. 
So, to avoid this we search for something that's not there.

That is if you seacrh from V1 for something that's not in the graph at all, then the algorithm is going to just keep searching and searching and building shortest paths to all the nodes it encounters along the way. 
Until it discovers that the node that it's looking for just isn't there. At the end of process, every single node in the graph will have a shortest path from the (will be notated, annotated with) the shortest path from V1 to that node.
So, the running time here is just the time it takes to do a single search, i.e. theta (n+m). Then you get the answer for all the nodes in the graph.