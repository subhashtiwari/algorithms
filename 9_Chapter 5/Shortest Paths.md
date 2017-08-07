To find the shortest paths we do depth first 

1. Start of at the starting node and add it to the open list.

2. Pull off the open list and add all the neighbours of Starting Node to the open list.

3. Then choose one of the nodes and unexpand neighbours to the graph. 

4. Do this with all others. Then we start from one of the neighbour that have the least weight. But if we still don't get the shortest path. 

5. Then we start off with the second least weighted neighbour, and follow step 3. If there is a path from there to ending point then we get the weight of entire path. 

6. Following this we get a node and pull off the open list and all its edges to the non-complete nodes.

7. Following all these steps we get shortest path from starting node to ending node.