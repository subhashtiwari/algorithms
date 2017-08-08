Dijkstra's Shortest Path Algorithm

Dijkstra was the first one to describe and analyze the algorithm for a single-source shortest path. 

Shortest distances form V: distance to V is 0 all other distances are unknown while not all nodes complete 
w = shortest known distance 
mark w known i.e. lock it down.
for all neighbours x of w if disance to w + weight(w,x) < known distance to x, then update x's distance.