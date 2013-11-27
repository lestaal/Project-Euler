### Problem 4 ###

def reverse(s):
    """ Returns the reverse of inputs string s"""
    result = ''
    for i in xrange(len(s)-1, -1, -1):
        result += s[i]
    return result

def largest_palindrome(digits):
    """
    Inputs: digits - integer greater than 1
    Outputs: largest palindrome number made from the product of two n-digit numbers
    """
    lower = 9
    upper = 99
    for i in xrange(digits-2):
        lower = int(str(lower)+'9')
        upper = int(str(upper)+'9')
    palindromes = set([])
    for i in xrange(upper, lower, -1):
        for j in xrange(upper, lower, -1):
            if str(i*j) == reverse(str(i*j)):
                palindromes.add(i*j)
    return max(palindromes)

def test_larg_pal():
    print largest_palindrome(2), '= 9009'
    
print largest_palindrome(3)
