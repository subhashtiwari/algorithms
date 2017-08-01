 Complete the intermediate steps
  - create_rooted_spanning_tree
  - post_order
  - number_of_descendants
  - lowest_post_order
  - highest_post_order

 And then combine them together in
 `bridge_edges`

 So far, we've represented graphs 
 as a dictionary where G[n1][n2] == 1
 meant there was an edge between n1 and n2
 
 In order to represent a spanning tree
 we need to create two classes of edges
 we'll refer to them as "green" and "red"
 for the green and red edges
 
 So, for example, the graph given in lecture
 G = {'a': {'c': 1, 'b': 1}, 
      'b': {'a': 1, 'd': 1}, 
      'c': {'a': 1, 'd': 1}, 
      'd': {'c': 1, 'b': 1, 'e': 1}, 
      'e': {'d': 1, 'g': 1, 'f': 1}, 
      'f': {'e': 1, 'g': 1},
      'g': {'e': 1, 'f': 1} 
      }
 would be written as a spanning tree
 S = {'a': {'c': 'green', 'b': 'green'}, 
      'b': {'a': 'green', 'd': 'red'}, 
      'c': {'a': 'green', 'd': 'green'}, 
      'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
      'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
      'f': {'e': 'green', 'g': 'red'},
      'g': {'e': 'green', 'f': 'red'} 
      }

