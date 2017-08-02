# Write a code that take a list L and the value and return a new list that has the property that V is in its final sorted place.

L = [31, 45, 91, 51, 66, 82, 28, 33, 11, 89, 84, 27, 36]

def partitioning(L, v)
    smaller = []
    bigger = []
    for val in L:
        if val < v: smaller += [val]  # Every time it gets a smaller than v, it puts it in smaller list.
        if val > v: bigger += [val]   # Every time it gets a bigger than V, it puts it in bigger list.
    return smaller + [v] + bigger

print partitioning(L, 84)


# The output is : [31, 45, 51, 66, 82, 28, 33, 11, 27, 36, 84, 91, 89]