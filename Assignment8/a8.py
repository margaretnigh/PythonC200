#############################################
# Problem 1
#############################################
def F(n,m,p):
    """

    Args: n,m,p postive ints

    Loops through function until p equals 0

    Returns: the total of induction steps, the base case to compute the functions

    """
    if p == 0:
        return 100 + n - m
    else:
        return n*m - p + F(n-3,m-2,p-1)
    pass

def Ft(n,m,p,v = 100):
    """

    Args: n,m,p ints, v = 100 int
    Loops through function until p equals 0, add accumulator each time
    Returns: Total accumulator num

    """
    if p == 0:
        return v + n - m
    else:
        return Ft(n-3,m-2,p-1,v=v + n*m - p)
    pass

def B(n):
    """

    Args: n: positive int

    Loops through function until n equals 0, returns base case to compute functions

    Returns: total induction num

    """
    if n == 0:
        return 5
    elif n == 1:
        return 10
    else:
        return 5*n + B(n-1)
    pass

def Bt(n,v=0):
    """

    Args: v = 0 int, n positive int
    Loops through function until n equals 0, adding to accumulator each time
    Returns: total accumulator num

    """
    if n == 0:
        return v + 5
    elif n == 1:
        return v + 10
    else:
        return Bt(n-1,v=v + 5*n)
    pass


def x(n):
    """

    Args: n positive int
    Loops through function until n equals 0, returns base case to compute
    Returns: total induction num

    """
    if n == 0:
        return 3
    elif n % 2 == 0:
        return 2*n + 1 + x(n-1)
    else:
        return 2*n + x(n-1)
    pass

def xt(n,v=3):
    """

    Args: n positive int, v = 3 int
    Loops through function until n equals 0, add to accumulator step each time
    Returns: total accumulator num

    """
    if n == 0:
        return v
    elif n % 2 == 0:
        return xt(n-1,v=v + 2*n + 1)
    else:
        return xt(n-1,v=v+2*n)
    pass

#############################################
# Problem 2
#############################################
d,c = "d","c"
def balance(xbook):
    """

    if initial list value is c or d, add to a different sum, compare
    Args: Xbook nested lists
    Returns: True or False boolean


    """
    sum1 = 0
    sum2 = 0
    for i in range(len(xbook)):
        for j in range(len(xbook[i])):
            if xbook[i][j] == "d":
                sum1 += xbook[i][1]
            elif xbook[i][j] == "c":
                sum2 += xbook[i][1]
    if sum1 == sum2:
        return True
    else:
        return False
    pass

def balance_rec(xbook):
    """

    if initial list value is c or d, adds or subtracts from the accumulator,
    if sum of accumulator = 0, sums are equal
    Args: Xbook nested lists
    Returns: True or False boolean


    """
    def bh(blst,a=0):
        if blst:
            if blst[0][0] == 'd':
                return bh(blst[1:],a=a + blst[0][1])
            if blst[0][0] == 'c':
                return bh(blst[1:],a=a - blst[0][1])
        if not blst and a == 0:
            return False
        else:
            return True

        pass

    return not bh(xbook)



#############################################
# Problem 3
#############################################
def gsf_close(a,r,n):
    """

   analytic summation to find integer
    Args:
    a positive int
    r positive int
    n positive int
    Returns: Positive int sum


    """
    return int((a*(1/(1-r)) * (1-r**n)))
    pass

def gsf(a,r,n):
    """

    mathematical summation and for loop to find integer
    Args:
    a positive int
    r positive int
    n positive int
    Returns: Positive int sum
    """
    sum = 0
    for i in range(n):
        if n > 0:
            sum += a*r**i
            n -= 1
            i += 1
    return sum

    pass

def g(a,r,n):
    """
    mathematical summation and recursion to find integer
    a positive int
    r positive int
    n positive int
    Returns: Positive int sum

    """
    def gh(k):
        """

        Args:


        Returns:

        """
        if k == 0:
            return a*r**k
        else:
            return a*r**k + gh(k-1)
 
 
    return gh(n-1)

#############################################
# Problem 4
#############################################
def occurs(x,xlst):
    """
    For loop implementation of occurance
    Args:
        x number
        xlst list of values

    Returns: boolean 
    """
    found = False
    for i in xlst:
        if x == i:
            found = True
            break
    return found

def occurs_w(x,xlst):
    """

    While loop of occurances
 
    Args:
        x num
        xlst list of values
 
    Returns: boolean


    """
    found = False
    i = 0
    while i < (len(xlst) - 1):
        i += 1
        if x == xlst[i]:
            found = True
            break
    return found

    pass

def occurs_r(x,xlst):
    """

    While loop of occurances
    Args:
        x num
        xlst list of values
 
    Returns: boolean

    """
    if xlst:
        return xlst[0] == x or occurs_r(x, xlst[1:])
    else:
        return False

    pass

#############################################
# Problem 5
#############################################
def gcd(x,y):
    """
    Finds Greatest Common Denominator of two numbers 
    induction steps using % until one is found
 
    Args:
    x positive int
    y positive int
 
    Returns: GCD


    """
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

    pass

if __name__ == "__main__": 
    # Problem 1
    print("The next 3 lines are calls for F and Ft")
    print(F(5,5,5),Ft(5,5,5))
    print(F(1,2,3),Ft(1,2,3))
    print(F(5,4,2),Ft(5,4,2))
    
    print("The next 5 lines are calls for B and Bt")
    for i in range(5):
       print(B(i), Bt(i))
       
    print("The next 5 lines are calls for x and xt")
    for i in range(5):
           print(x(i),xt(i))

    # Problem 2  
    d,c = "d","c"
    xbook1 = [[d, 895],[c,7500],[d,339],[c,234],[d,6400],[d,100]]
    xbook2 = [[d, 95],[c,500],[d,39],[c,234],[d,600],[d,10]]
    print(balance_rec(xbook1),balance(xbook1))
    print(balance_rec(xbook2), balance(xbook2))

    # Problem 3
    print(gsf(2,3,5))
    print(g(2,3,5))
    print(gsf_close(2,3,5))

    #Problem 4
    print(occurs(1,[2,3,4]),occurs_w(1,[2,3,4]),occurs_r(1,[2,3,4]))
    print(occurs([1],[1,3,4]),occurs_w([1],[1,3,4]),occurs_r([1],[1,3,4]))
    print(occurs([1],[1,[1],2]),occurs_w([1],[1,[1],2]),occurs_r([1],[1,[1],2]))

    # Problem 5
    print(gcd(10,6))
    print(gcd(12,9))
    print(gcd(55,40))

