Now we have to find if the Clique Problem lies in NP.
The problem is : GIven a graph G and number k, is there a clique of size k in G?

For a problem to be in NP the problem needs to have two things:

1. A short accepting certificate and 
2. It needs to have a fast verification algorithm. 

There is no requirement of a solution to this problem that's fast.We just need to show that the certificate verification algorithm is fast.

The certificate in this case is : Set of nodes in Clique.

The verification algorithm that we run is that we go through all pairs of nodes in that certificate, and make sure that in the original graph G, they're originally connected. 
Each of these test takes unit time and its of the order of theta(k^2) pairs to check.

So, for every graph G that has a clique, there is a certificate that would cause the verification algorithm to say yes, but for any graph G that doesn't have a k clique, there's no certificate that would cause the verification algorithm to say yes.

Make sure the cirtificate that is given have k nodes.