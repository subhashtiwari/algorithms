def makeG(N):
    if n == 1:
        return <a single node>
    g1 = makeG(n / 2)
    g2 = makeG(n / 2)
    for i in range(log(n)):
        i1 = <random node from g1 without replacement>
        i2 = <random node from g2 without replacement>
        make_link(G, i1, i2)
    return G


# For this code T(n) = theta(n log(n))

# As for first level (n) : log(n)
# Second level (n/2) : log(n/2) + log(n/2) = 2 log(n) - 2
# Third Level (n/4) : 4 log(n) - 4

# n level (n/n) : n log(n) - n
# Adding all levels...
# (n log(n) - n) + (n/2 log(n) - n/2) + (n/4 log(n) - n/4)+ ... + log(n) = 2n log(n) - 2n = theta (n log(n))
