### Problem 16 ###
    
def power_sum(base, exp):
    """
    Inputs: base - integer, exp - integer
    Outputs: sum of the digits of base ** exp
    """
    n = base ** exp
    result = 0
    for i in xrange(len(str(n))):
        result += int(str(n)[i])
    return result

def test_power_sum():
    """ test function power_sum """
    print power_sum(2, 4), "= 7"
    print power_sum(7, 2), "= 13"

print power_sum(2, 1000)
