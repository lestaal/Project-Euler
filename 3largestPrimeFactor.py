### Problem 3 ###
# What I referenced:
# http://stackoverflow.com/questions/23287/prime-factors

def largest_prime_factor(num):
    """
    Inputs: num - positive integer to find largest prime factor of
    Outputs: largest prime integer factor of num
    """
    factors = [num]
    while factors:
        largest = factors.pop(factors.index(max(factors)))
        i = 2
        prime = True
        while i <= int(largest/2):
            if (largest%i == 0):        
                factors.append(i)
                factors.append(largest/i)
                prime = False
                break
            i += 1
        if prime:
            return largest

def test_largest_prime_factor():
    """ test function largest_prime_factor
    Inputs: none
    Outputs: none, prints results
    """
    print largest_prime_factor(9), '= 3'
    print largest_prime_factor(21), '= 7'
    print largest_prime_factor(38), '= 19'
    print largest_prime_factor(13195), '= 29'

print largest_prime_factor(600851475143)
