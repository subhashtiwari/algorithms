Depth versus Breadth First Search

To know how to find shortest paths in a graph, it's going to help to compare a little bit between the kinds of depth first search algorithms with the kinds of breadth first search algorithms.  

Let's consider this algorithm:
check_connection(G,'i','n')

If we take the graph in image Connection and ask the check_connection algorithm to check the connection between i and n, the flow of control or the steps it takes to check the connection are as follows:

check_connection(G,'i','n')
    mark_component(G,'i',marked)
        mark_component(G,'j',marked)
            mark_component(G,'k',marked) 
                and so on.

Essentially, the path that it followed to get to n is 1,2,3,4,5 links long which is not the represtative of the shortest path, which in this case is just the 1 link.

We start at i and check the things that are close to i before the things that are far from i. 
This is what breadth first search is going to do.