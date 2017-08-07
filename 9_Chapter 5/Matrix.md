Matrix Multiplication

A graph can be represented on a set of nodes as a matrix, it's a matrix that consists of 0s and 1s and if it's a sparse graph, then mostly zeros.

If there's a link between node i and node j, then the corresponding position in the matrix has a number in it, number1. 1 means there is a link from i to j. 

The graph in this study are bidirectional. So, if there's a 1 in this i-j position, then there is also a 1 in j-i position. It means that the matrix is symmetrical.
It means that its transpose is same as the original one.

For Multiplication

Take the i th row of the first matrix and j column of the second matrix. Then go across the row and down the column, one element at the same time.

In this case if there is 1 on both side then only the product is 1 otherwise it is zero.
It will give the number of vectors that are in the exact same positions.
To understand more easily, there is a path from i to k and k to j, such that we can get from i to j from k. 
The multiplication will add all such paths. 

The running time of this process is n^3. 
If the matrix is a sparse matrix then it is n^2.