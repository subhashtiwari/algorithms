Clique is a set of nodes in a network thatare all pairwise connected.

So, for a graph G, shown in image Clique, and number k, let's say 4, is there a clique of size k in G.
Find if there is any four clique, if yes then add the node numbers that make up the clique together.

Four clique means that there are 4 element in the given clique that are connected to each other. 

The answer is 16. 
As for a 4 clique the nodes that are part of it have to be degree of at least 3. So it removes 2 and 6 as there degree is 2. 
Now, if 4 is the part of clique, then it's neighbours have to be the rest of the clique i.e. 1, 3 and 8. But that's not as 8 is not connected to 1 directly. 
So can't be part of 4 clique. And it also removes 8, as 8 is now have a degree of 2.

So only possibily left is 1, 3, 5 and 7 and they all are connected to each other, and theer sum is the answer.