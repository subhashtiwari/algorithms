The important property of a heap is that the smallest value of all has to be at the top. Because a node can't be below anything larger than that. So, the only place for it, is to be at the top. 
The second smallest value will be immediately below it. 

As the nodes are filled in a tree from top to bottom and left to right, the nodes can be numbered. 

As these nodes go in a sequence there a way to find out the level, the n parent of a child, the right/left child of a parent so easily. 

The child numbers are
- for left child, it's always the node number doubled plus one. i.e. 2i + 1.

- for the right child its 2i + 2, as it's adjacent to the left one.

To find the parent node of ith node. Round off (i - 1)/2. 