# Write a python code to create a Combination Lock given a list of nodes

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        (G[node2])[node1] = 1
        return G

# This is the main
def create_combo_lock(nodes):
    G = {}                                      # Empty graph created.
    make_link(G, nodes[0], nodes[1])            # Create a length between zero node and the first node.
    for i in range(2, len(nodes)):              # This loop will run throught the rest of the nodes.
        
        make_link(G, nodes[i-1], nodes[i])      # Here, we make a chain connecting the first node with the second node, second with the third and so on.
        
        make_link(G, nodes[0], nodes[i])        # Here, we create the star part connecting zero node with the second node, zeroth node with the second node and so on till last node.

    return G


### ### ### ###

# Code for Testing if the Combination Lock is correct.

def is_chain(graph, nodes):
    # find the first node with degree one
    start = (n for n, e in graph.iteritems()
             if len(e) == 1).next()
    count = 1
    # keep track of what we've seen to make
    # sure there are no cycles
    seen = set([start])
    # follow the edges
    prev = None
    current = start
    while True:
        nexts = graph[current].keys()
        # get rid of the edge back to prev
        nexts = [n for n in nexts if not n == prev]
        if len(nexts) > 1:
            # bad.  too many edges to be a chain
            return False
        elif len(nexts) == 0:
            # We're done following the chain
            # Did we get enough edges:
            return count == len(nodes)
        prev = current
        current = nexts[0]
        if current in seen:
            # bad.  this isn't a chain
            # it has a loop
            return False
        seen.add(current)
        count += 1

def is_combo_lock(graph, nodes):
    # first see if we have a star
    center = None
    degree = None
    for node, edges in graph.iteritems():
        if len(edges) > degree:
            center = node
            degree = len(edges)
    if not degree == len(nodes) - 1:
        return False
    # make a graph out of all the edges
    # not connected to the center
    chain = {}
    for node, edges in graph.iteritems():
        if node == center:
            continue
        for e in edges:
            if e == center:
                continue
            make_link(chain, node, e)
    return is_chain(chain, [n for n in nodes if n != center])

def test():
    for n in [5, 10, 20]:
        combo = create_combo_lock(range(n))
        if not is_combo_lock(combo, range(n)):
            return False
    return True