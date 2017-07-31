These edges are those edges which connect one network to another and if removed there will be two different networks formed having no connection between them.

To find the bridge edge, we follow some steps

1. Write the graph as a tree. Picking any one node, except any node that is part of bridge edge.

2. Post order the nodes : We do this by following a rule i.e. the parent will only be numbered when all its children are numbered on both sides. In case of multiple branches we proceed from left to right.
An image named Bridge shows the result of post order.

3. Compute the number of decendents for each node : The number of decendents are the number of nodes that are either the node or reachable from the node by following green edges only.

L - lowest : green or one red : We consider the set of nodes that are descendents of the node or reachable from the descendent of the node by one hop of a non-tree edge and of all those  nodes that are reachable, we're going to look at the post-order value that is the smallest. It is called L.

H - highest : green or one red : It is the same idea as that of the previous one.

Bridge edge : Now we find which one them is the bridge edge. Now with the help of image Bridge we find out he Bridge edges.

1. All the bridge edges are the ones that are green, 
2. The green number is less than or equal to black number, and 
3. The red number is bigger than the blue number minus the black.

OR 

1. The H value has to be less than or equal to the post order value, 
2. The L value has to be bigger than the number of descendents minus the post order value. 