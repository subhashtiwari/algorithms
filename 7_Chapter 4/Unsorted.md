Statistics on Unsorted Lists

If the list is unsorted we can perform two funtions to get the statistics.

1. Sort the list first : The list can be sorted and then various statistics can be solved.
Sorting a list of length n takes theta(n logn) time for execution.
This is a very long time as we have to run through the list repeatedly log n times essentially.

2. Other way is to extract the statistics that we're looking for in effectively one scan through the data.
So, the running time will be theta(n).
By this we can get maximum, minimum and median also.

The mean or average of the list is the sum over all the elements on the list from 0 to n-1 and then divide by the number of values.
It is represented by mu.