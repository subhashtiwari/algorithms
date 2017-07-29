For the following networks write there degree and path withrespect to the theta functions.
1. Clique

Degree is linear so theta(n) : As each node is connected to another node.
Path is theta(1) : As there is only single path to get from one node to any other node.

2. Ring

Degree is constant so theta(1) : As each node has a degree of 2.
Path is theta(n) : As the longest path is linear in nature.

3. Balanced Tree

Degree is constant so theta(1) : As a node might have a parent and two children. The root nide has a degree of 2 and all the leaves have a degree of 1, so it's never more than 3.
Path is theta(log n) : As any node can get to anyother node by going up to the root and then back down to the node you want to get to.

4. Hypercube

Degree is theta(log n) : As each node is numbered with log n bits and is connected to all other nodes in the network that have names differ by at most one bit. So each node is connected to another log n nodes.
Path is theta(1) : As suppose we want to get from 010 and 110 then we need to change one bit to do this. 
