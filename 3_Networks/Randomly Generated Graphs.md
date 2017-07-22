These graphs are generated according to the Erdos - Renyi Model.

It works as follows :

Lets imagine that we have some graph with n nodes or we have some set of n nodes, and we have some 
probability p it is called connectivity probability.

The Generation Process works as follows :
1. Generate n nodes with no edges at all.
2. Then loop through all possible pairs of nodes i, j. But we only connect them after flipping a coin,
that comes up heads with probability p. If it does come up heads, we connect the pair. Otherwise, we don't.