There are some poof related to bridge edges.

1. No non tree edge is a bridge. It should be green edge not the red one. Because the red edges are the ones that get added for a node that has already been reach out by the graph. So, the red edges can't be bridge edges.

2. We can test whether or not a given node is in the subtree rooted at some node. If it is at the bridge edge than by the algorithm of numbering according to post order it should be less than any of its sub nodes.

3. If not a bridge edge, non tree edge, red ones causes L or H values to go outside the valuesin the subtree.