"""We generate a list of triples for hailstone seeds, showing seed, length, height.

Usage: import triples
Usage: from triples import triples

>>> triples(1, 6)
[(1, 1, 1), (2, 2, 2), (3, 8, 16), (4, 3, 4), (5, 6, 16), (6, 9, 16)]

"""

import height
import length


def triples(minseed, maxseed):
    """Returns a list of triples(seed, length, height) for all seeds from minseed to maxseed.

    """

    # Replace the pass below with your own code.
    global mylist
    mylist=[]
    for n in range(minseed, maxseed + 1):
        mylist.append((n, length.measure(n), height.measure(n)))
    return mylist
