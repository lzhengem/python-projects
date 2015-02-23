"""Calculates how high the hailstone numbers get for a given seed.

Usage: import height
Usage: from height import measure
Usage: from height import measures

>>> measure(5)
16
>>> measure(7)
52
>>> measure(1)
1
>>> measures(6)
[(1, 1), (2, 2), (3, 16), (4, 4), (5, 16), (6, 16)]

>>> measures(5)

"""

from hailstones import stones
from formulas import ulam

def measure(seed):
    """ For a given seed, returns the biggest of the stones.

    """

    # Replace the pass below with your own code.
    global max
    max = ulam(seed)
    numbers = stones(seed)

    for number in numbers:
        if number > max:
            max = number
    return max

def measures(maxseed):
    """Returns a list of pairs (seed, measure) for all seeds from to maxseed.

    For example:
    >>> measures(6)
    [(1, 1), (2, 2), (3, 16), (4, 4), (5, 16), (6, 16)]

    
    """

    # Replace the pass below with your own code.
    mylist = []
    for n in range(1, maxseed + 1):
        mylist.append((n,measure(n)))
    return mylist
        
  

