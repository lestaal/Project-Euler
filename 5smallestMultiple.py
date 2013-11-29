### Problem 5 ###

def smallest_multiple(num):
    """
    Input: num - positive integer
    Output: smallest integer that is evenly divisible by all integers from 1 to num
    """
    mult = num
    while 1:
        satisfied = True
        for i in xrange(num-1, 1, -1):
            if mult%i != 0:
                satisfied = False
                break
        if satisfied:
            return mult
        mult += num

def test_smallest_multiple():
    """ test function smallestMultiple
    Input: none
    Output: none, prints results
    """
    print smallest_multiple(4), '= 12'
    print smallest_multiple(5), '= 60'
    print smallest_multiple(10), '= 2520'

test_smallest_multiple()
print smallest_multiple(20)
