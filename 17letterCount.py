### Problem 17 ###

def numberLetterCount(limit):
    """
    Inputs: limit - integer divisible by 100 that is less than or equal to 1000
    Outputs: amount of letters (no spaces or hyphens) to write out all numbers from 1 to limit
    """
    word = {0:'', 1: 'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',
            10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',
            20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'
            }
    c = 0
    for i in xrange(1,20):
        c += len(word[i])
        if i == 9:
            ones = c
    undertwenty = c
    hundreds = limit/100
    count = undertwenty*hundreds
    twentyto99 = 0
    for i in xrange(20, 91, 10):
        twentyto99 += len(word[i])*10 + ones
    count += twentyto99*hundreds
    for i in xrange(1, hundreds):
        count += len(word[i])*100 + len('hundred')*100 + len('and')*99
    if limit == 1000:
        count += len('onethousand')
    return count

print numberLetterCount(1000)   
