Depth first search is that it can be implimented really straightforwardly with recursion, which makes it very easy to read and easy to reason about.
But not so with breadth first search. It require to implement it in away that keeps track things in the right order.

Now we are going to do Depth first search without recursion but by using a new data structure called the open list.
Open list is a kind of a "to do list" because it kepps track of what it is needed to do next. Otherwise it will perform some other task that is not reqiured.
So, to keep it from being astray we use open list. 

The process it follows is shown below:

1. Grab last element of open list.
2. Mark any unmarked neighbours and add to open list.
3. Repeat until nothing open. 

It just dives deeper into the graph and identifies each and every element.

