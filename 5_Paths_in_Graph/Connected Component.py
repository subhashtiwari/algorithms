# This is a Python Code to solve the Problem of connected Component Shown in the image Connected.

# The Edge Maker

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1

    return G

connection = [('a','g'),('a','d'),('d','g'),('g','c'),
               ('b','f'),('f','e'),('e','h')]

G ={}
for (x,y) in connections: make_link(G,x,y)


#Traversal...
#Call this routine on nodes being visited for the first time        
def mark_component(G, node, marked):
    marked[node] = True
    total_marked = 1
    for neighbour in G[node]:
#        print "=>", neighbour, "(",node,")"
        if neighbour not in marked:
            total_marked += mark_component(G, neighbour, marked)
        return total_marked

def list_component_sizes(G):
    marked = {}
    for node in G.keys():
        if node not in marked:
            print "Component containing ", node, ": ", mark_component(G, node, marked)

list_component_sizes(G)    


## OUTPUT ##
# Component containing a : 4  
# Component containing b : 4

 