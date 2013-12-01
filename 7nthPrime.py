import math

### Problem 7 ###

def is_prime(num):
    """
    Inputs: num - integer
    Outputs: True if num is prime, False otherwise
    """
    if num == 1: return False
    elif num < 4: return True # 2 and 3 are prime
    elif num%2 == 0: return False
    elif num < 9: return True # 5 and 7 are prime
    elif num%3 == 0: return False
    else:
        for i in xrange(5, int(math.sqrt(num))+1, 6):
            if num%i == 0: return False
            if num%(i+2) == 0: return False
        return True

def prime(n):
    """
    Inputs: n - positive integer
    Outputs: the nth prime
    """
    if n == 1: return 2
    elif n == 2: return 3
    count = 2
    coef = 1
    while count < n:
        if is_prime(6*coef - 1):
            curr = 6*coef - 1
            count += 1
            if count == n: return curr
        if is_prime(6*coef + 1):
            curr = 6*coef + 1
            count += 1
        coef += 1
    return curr

def test_prime():
    """ test function prime
    Inputs: none
    Outputs: none, prints results
    """
    for i in xrange(1, 10):
        print prime(i)
    print prime(1000), '= 7919'

print prime(10001)
