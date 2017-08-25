
# take one month to reach reproductive maturity
# n - # of months
# k - # of pairs in litter
# for loop function for only the total
def fib(n,k):
    # total number of rabbit pairs
    a,b = 1,1
    for i in range(n-1):
        a,b = b, b+(a*k)
    return a

print(fib(34,4))