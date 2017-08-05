A heap is a particular data structure.  It is used to implement a "priority queue" which is abstract data type. 

It supports three different operartions.

1. Insert : TO insert an element in an ordered list takes time of theta(n). For an un-ordered list it takes theta(1) time to insert an element.

2. Find min : It takes runnig time of theta(1) to find an element in an ordered list. But in an unordered list it takes theta(n) time.

3. Remove min : It takes runnig time of theta(1) to remove the element. But for an un-ordered list it takes theta(n) time.

It is a bunch of values that are arranged in a kind of graph specifically it's a balanced binary tree and each of the nodes has a value in it.

Heap property : The value in a node is no bigger than the values of the children. Due to this as we traverse down the tree we're traversing down the sorted list.

The height of a heap from root to leaf is theta(logn).

The nodes are filled in a tree from top to bottom and left to right.