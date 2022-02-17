###########################################################
# factorial
###########################################################
import time
start = time.time()
def factorial(n):
    """
    Recursive function to calculate the factorial of n

    Input:
        n (an integer)
    Returns:
        n! = n*(n-1)*...*2*1
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    pass
end = time.time() - start
print(factorial(900))
print(end)

def tail_factorial(n, a=1):
    """
    Tail-recursive function to calculate the factorial of n

    Input:
        n (an integer)
    Returns:
        n! = n*(n-1)*...*2*1
    """
    if n == 0:
        return a
    else:
        return tail_factorial(n-1, a=a*n)
    pass

d = {}
def memo_factorial(n):
    """
    Memoized function to calculate the factorial of n

    Input:
        n (an integer)
    Returns:
        n! = n*(n-1)*...*2*1
    """
    if n not in d.keys():
        if n <= 1:
            d[n] = 1
        else:
            d[n] = n * memo_factorial(n-1)
    return d[n]
    pass

###########################################################
# only_ints
###########################################################

def only_ints(xlist):
    """
    Recursive function to return a list with all non-ints taken
    out of it.

    Input:
        xlist - a list of elements
    Returns:
        xlist, but with only the 'int'-type elements kept.

    """
    if xlist == []:
        return[]
    elif type(xlist[0]) != int:
       return [] + only_ints(xlist)
    else:
        return [xlist[0]] + only_ints(xlist[1:])
    pass

print(only_ints([2,"r",5]))

def tail_only_ints(xlist, a=[]):
    """
    Recursive function to return a list with all non-ints taken
    out of it.

    Input:
        xlist - a list of elements
    Returns:
        xlist, but with only the 'int'-type elements kept.

    """
    if xlist == []:
        return a
    elif type(xlist[0]) != int:
        return only_ints([] + xlist[1:])
    else:
        return only_ints(xlist[1:], a = [xlist[0]] + a)
    
    pass

d = {}
def memo_only_ints(xlist):
    """
    Recursive function to return a list with all non-ints taken
    out of it.

    Input:
        xlist - a list of elements
    Returns:
        xlist, but with only the 'int'-type elements kept.

    """
    xtup = tuple(xlist)
    if xtup not in d.keys():
        if xlist == []:
            d[xtup] = []
        elif type(xlist[0]) != int:
            d[xtup] = memo_only_ints(xlist[1:])
        else:
            d[xtup] = [xlist[0]] + memo_only_ints(xlist[1:])
    return d[xtup]
    

if __name__ == "__main__":
    # Write your own print statements here
    # to briefly test your code
    pass