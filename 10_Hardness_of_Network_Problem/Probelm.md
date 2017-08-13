S - Independent set problem 
Find the strangers

Given graph H and number S is there a set of nodes of sizes S in H such that no two nodes in the set are connected in H. They are independent of each other.

How a polynomial solution to K-clique solves the S-independent set problems?
It can be done if we assume G to be complement of H. Then run S-clique on G, return answer.

The solution is shown using an image Reducing to Clique.

In this the complement of graph H is G, such that if there is connection between two nodes in Graph H then in Graph G there will be no connection between those nodes.
And if in Graph H there is not a connection between two nodes then in Graph G there will be connection between two nodes.

Now the new graph G, the complement of H has an S-clique if and only if H has an S independent set.

In the image Reducing to Clique as Graph G has all the pairwise edges then it has to fail to have all those pairwise edges in H.
# That's how we can use the solution into the clique problem to solve the independent set problem.