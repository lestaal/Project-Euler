import math

### Problem 10 ###

def is_prime(n):
    """ Improved version of is_prime
    Inputs: n - integer
    Outputs: True if n is prime, False otherwise
    """
    if n == 1: return False
    elif n < 4: return True # 2 and 3 are prime
    elif n%2 == 0: return False
    elif n < 9: return True # 5 and 7 are prime
    elif n%3 == 0: return False
    else:
        for i in xrange(5, int(math.sqrt(n))+1, 6):
            if n%i == 0: return False
            if n%(i+2) == 0: return False
        return True

def prime_sum(limit):
    """
    Inputs: limit - positive integer
    Outputs: integer sum of all primes less than limit
    """
    if limit == 2: return 2
    if limit <= 4: return 2 + 3
    coef = 1
    result = 2 + 3
    while coef < 100000000:
        if is_prime(6*coef - 1):
            if 6*coef - 1 > limit:
                return result
            else:
                result += 6*coef - 1    
        if is_prime(6*coef + 1):
            if 6*coef + 1 > limit:
                return result
            else:
                result += 6*coef + 1 
        coef += 1

def test_prime_sum():
    """ test function primeSum
    Inputs: none
    Outputs: none, prints results
    """
    print prime_sum(2), '= 2'
    print prime_sum(4), '=', 2+3
    print prime_sum(10), '=', 2+3+5+7
    print prime_sum(29), '=', 2+3+5+7+11+13+17+19+23+29

print prime_sum(2000000)
