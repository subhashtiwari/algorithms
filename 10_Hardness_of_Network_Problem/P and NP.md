There are two classes P and NP related to the Polynomial time Decideable problems.

P : polynomial-time decideable problems

If there is an algorithm for that problem such that when input size is n, the running time for solving that problem is in Big O(n^k) for some constant k.
So, there has to some kind of polynomila upper bound of an algorithm to solve that problem to be in P.

The constant k is allowed to vary with the class of teh problem, but any particular instance needs to be solved into the k.

Running times like theta(logn) belong to the category of big O(n^k) for some k, such as k=1.


NP : Non-deterministic Polynomial Time Decidable Problems

It is a problem that can be dissolved by a program that runs in polynomial time but has non-deterministic elements in it.

A problem is in NP if it has a short accepting certificate.
Accepting certificate is information that can be used quickly to show that the answer is "yes" (if it actually is yes).
Short means polynomial size and quickly means polynomial time.

A problem is in NP if there's a verification algorithm A. A is like a subroutine in a program.
Such that for any input for the problem that is a yes, there is a certificate C such that size of C is polynomial in the size of x, and the verification algorithm will say "yes".
But for any x that is a no, there is no certificate C that's polynomially sized with respect to x and the verification algorithm says "yes", so for any yes answer to the problem, a verification algorithm will say "yes" for some small cerificate, otherwise, it'll say "no" for all small ceritificate.

Sudoku problem is a perfect example of this, for any SUdoku problem that is solvable, there is some grid that we solve it, but for any problem that it's not solvable, there is no way that it can be filled with numbers. So the verification algorithm will say that it's okay.
The Sudoku problem says, "Is there a way of filling it in?" And the certificate that is used fits in both part of the definition, so it's a NP.


# The P is contained in NP, the reason is if the problem that we have can be decided by some polynomial time algorithm s that takes the input, runs in a polynomial time, and either says yes or no for that input.
# Then we can design for any input x, there's some certificate that makes it say yes, for any certificate, because if the answer is yes, it's always going to return yes. And if the answer is no there's no ceertificate you can give it that would get it to say anything other than no.

# So anything in P is also an NP.