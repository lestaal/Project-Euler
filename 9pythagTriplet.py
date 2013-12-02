### Problem 9 ###
# equations via Wolfram Alpha

def special_pythag_triplet():
    for i in xrange(1, 10000):
        if i == 1000: continue
        
        if (float(1000*(i-500))/(i-1000))%1 == 0 and (float(i**2 - 1000*i + 500000)/(1000 - i))%1 == 0:
            return i * (1000*(i-500))/(i-1000) * (i**2 - 1000*i + 500000)/(1000 - i)

print special_pythag_triplet()
