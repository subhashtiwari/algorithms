##This is another way to solve the problem of Eulerian Graph.

def get_degree(graph):
    degree = {}
    for x, y in graph:
        degree[x] = degree.get(x, 0) + 1
        degree[y] = degree.get(y, 0) + 1
    return degree
    
def eulerian_tour_is_possible(graph):
    degree = get_degree(graph)
    odd = 0
    for entry in degree: 
        if degree[entry] % 2 != 0: 
            odd += 1
    if odd == 0: return True
    return False

def find_next_edge(node, graph):
    edges = find_all_edges(node, graph)
    for edge in edges:
        if node in edge:
            return edge
    return None
        
def find_all_edges(node, graph):
    edges = []
    for edge in graph:
        if node in edge:
            edges.append(edge)
    return edges
            
def find_eulerian_tour(graph):
    if eulerian_tour_is_possible(graph):
        for i in range(len(graph)):
            tour = []
            graph_copy = graph[:]   # make copy of graph to do work on
            start_edge = graph_copy.pop(i)   # change starting edge as loop iterates
            tour.append(start_edge[0])
            tour.append(start_edge[1])
            while len(graph_copy) > 0:
                edge = find_next_edge(tour[-1], graph_copy)
                if edge == None: break  # we've reached a node where no more possible edges exist
                if tour[-1] == edge[0]:
                    tour.append(edge[1])
                else:
                    tour.append(edge[0])
                graph_copy.pop(graph_copy.index(edge))
            if graph_copy == []: return tour # we've used all edges, tour found! 
        return None 
    else:
        return None
