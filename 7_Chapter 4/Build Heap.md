In this we Build a Heap of a tree with seven nodes filled with random two digit numbers.
For an example an image named Build Heap1 is shown.

To do it we follow a procedure:

1. We start of at the root which is node zero. To do this we first heapify its two childs.

2. To make its childs into a heap we do it recursively. 

3. So, if anything that is a leaf we're done there. 

4. Then we move to there parent and if its not satisfy heap condition then swap it with a smaller child. 

5. Repeat the step 4 util we reach the bottom again. 

The result of the final heap is shown in image Build Heap2.

The running time is big O (n logn) or theta(n). 