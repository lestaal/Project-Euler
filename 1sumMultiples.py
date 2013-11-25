import math

### Problem 1 ###

def sum_multiples(multiples_of, limit):
    """
    Inputs: multiples_of - set of integers, limit - integer
    Outputs: integer sum of all multiples of integers in multiples_of
             that are less than limit
    """
    result = 0
    for i in xrange(limit):
        for mult in multiples_of:
            if i%mult == 0:
                result += i
                break
    return result

def test_sum_multiples():
    """ Test function sum_multiples
    Inputs: none
    Outputs: none, prints results
    """
    test = sum_multiples(set([3, 5]), 10)
    print test == 23, '%d = 23'%test

print sum_multiples(set([3, 5]), 1000)
