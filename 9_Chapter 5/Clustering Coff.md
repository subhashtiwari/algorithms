The earlier code to find the exact clustering coefficient takes was on average was linear in the size of the list.
But in real social network problems we just to calculate the approximate clustering coefficient to find whether it is heavily clustered or loosely clustered or slightly more clustered from the other database or not.

As in the code for calculating clustering coefficient it actually takes square of the degree to compute it. So, if  the degree is high or if there are not that many edges like star graph than it theta(n^2). 
And if it is densely connected graph like a clique than it will be theta(n^3) that is high. 

The formula for calculating clustering coefficient is shown in image Clustering Coeff.
This formula sum all the nodes in the graph, average it for n nodes in the graph. Then for each of those sum up all the pairs of nodes that are neighbours of the node v. Sum up whether or not they are connected than scale that by taking the number of possible connections 2 over neighbour size of v times the neighbour size of v minus 1.

