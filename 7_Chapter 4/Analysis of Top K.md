Its the analysis of running time of Top K algorithm.
As it is a recursive algorithm, it's going to help to set up in terms of recurrence relations.

The time it takes t run top K via partitioning one element. T(1) = 1

The time it takes to run an n element T(n) <= n + 1/2 T(n/2) + 1/2 T(n-1).

First it does the partitioning operation, which runs all through the elements of the list, that takes time n and then it recurse if it didn't get the result that covers up the less than part.
The partitioning algorithm splits the list L into a left and a right. But its not know which one it's going to recurse on and which one is bigger. So, there are two probabillities of 1/2 each that either one of the halves right or left is bigger, bigger means its going to be at least size n/2.

If the recursive algorith gets called on the smallest half then the work it has to do is whatever the recursive running time is on at least of size n/2, or smaller as this is an upper bound and that happens with the probability of half, but it can be unlucky and have to recurse on the larger half, which could involve actually almost the size of the entire list. 
It's kind of a wierd recurrence relation because it has probabilities in it.

# It's going to take 4n, as a good upper bound on the value of T(n).#
It can be proved by induction as if you put n then we get  =  n + 1/2 2n + 1/2 4n
                                                           = 4n  
Thus it is proved that the upper bound is 4n. Also it is cler that it is theta(n).                                                       