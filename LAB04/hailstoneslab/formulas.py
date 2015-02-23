"""Formulas used for calculating hailstone numbers.

Usage: from formulas import ulam

>>> ulam(5)
>>> 16
>>> ulam(7)
22
    
"""

def ulam(n):
    """Returns the next hailstone number after n.
    """

    # Replace the pass below with your own code.
    if n ==1:
        return 1
    elif n % 2 == 1: #odd
        return 3*n + 1
    else:           #even
        return n//2

