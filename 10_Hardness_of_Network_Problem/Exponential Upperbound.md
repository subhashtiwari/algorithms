There is a relationship between the class NP and the cluster problems that are solvable in exponential time.
Any problem that's in NP is also going to be solvable in exponential time.
So, the set of exponential time solvable problems also includes NP. It means that it takes at most exponential time.

So, if the problem is in NP that means that there's a bound on the size of the certificate needed.

- n^c : bound on certificate size. Where n is related to the size of the input and c is some constant that depend on the problem.

- n^k : bound on running time of the verification algorithm. Where n is the size of input and k is some constant that depend on the problem but it can't depend on the input.

If we have these two than an algorithm can be made that can solve the problem for any input.
We can run through all the certificates that could possibly be relevant for input x and for each one run the verification algorithm, and if the verification algorithm that's something that shows that x is true, then return true as the solution for the problem and if we through all the possible certificate and none of them made the accepting, the verification true then we can return false.

The running time of this algorithm is theta(n^k 2^(n^c)).
As the number of times we go to this loop is like 2 to the n to the c, i.e. 2^n^c. This is the number of different assignments of bits to the certificate of this size. And for the if function it is n^k.
So, the total running time is exponential.