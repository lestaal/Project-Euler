import math

### Problem 15 ###

def lattice(n):
    """
    Returns number of routes to travel from upper left corner to lower right corner of
    an n-by-n lattice only being able to move down and right.
    """
    # need the number of unique sequences of length 2n consisting of n downs and n rights
    return math.factorial(2*n)/(math.factorial(n)**2)

def brute_force_lattice(n):
    """ Inefficient!
    Returns number of routes to travel from upper left corner to lower right corner of
    an n-by-n lattice only being able to move down and right.
    """
    import itertools
    s = ''
    for i in xrange(n):
        s += 'RD'
    paths = set([])
    for i in itertools.permutations(s):
        paths.add(i)
    return len(paths)

def test_lattice():
    """ test function lattice
    Inputs: none
    Outputs: none, prints results
    """
    print lattice(2), '= 6'
    print lattice(3), '=', bruteForceLattice(3)
    print lattice(4), '=', bruteForceLattice(4)
    print lattice(5), '=', bruteForceLattice(5)
    
print lattice(20)
