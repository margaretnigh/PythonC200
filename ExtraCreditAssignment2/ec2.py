import random as rn
import math
from typing import Coroutine, Counter

#############################################
# Problem 1
#############################################
def lr(xlst):
    """
    TODO:
    
    Implement function described in the homework PDF
    """ 
    count = 0
    counts = []
    for i in range(len(xlst)):
        if xlst[i] == 1 and xlst[i+1] == 1:
            count += 1
        else:
            count = 0
        counts.append(count)
        
    #find max
    max = counts[0]
    for x in counts:
        if x > max:
            max = x
    return max+1



#############################################
# Problem 2
#############################################
def nn(x,y,z):
    """
    TODO:
    x is the list of numbers
    y is the number to be nearest to
    z is how many
    Implement function described in the homework PDF
    """ 
    new_list = []
    temp = []

    #loop through and compare the target y to x[i]
    for i in range(len(x)):
        diff = abs(y - x[i])
        temp.append([x[i],diff])
    
    while z > 0:
        min1 = temp[0][1]
        for j in range(len(temp)):
            # If the other element is smaller than first element
            if temp[j][1] < min1:
                min1 = temp[j][1] #It will change
                num = temp[j][0]
        new_list.append(num)
        temp.remove([num,min1])
        z = z - 1
    return new_list
  

         


#############################################
# Problem 3
#############################################
#Assume this is in 2D dimension
def distance(p1,p2):
    """
    TODO: 
    Given two points, find the distance between the points.
    The points are given as a tuple with 2 values
    """
    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    y2 = p2[1]
    dist = math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))
    return dist

def brute(xlst):
    """
    TODO:
    Given a list of points, where each points is represented 
    by a tuple of 2 values.

    returns a list [x,y,d]:
        x is the first pair
        y is the second pair
        dis the smallest distance between x and y
    """
    new_list = []
    for i in range(len(xlst)-1):
        p1 = xlst[i]
        p2 = xlst[i+1]
        dist = distance(p1,p2)
        new_list.append([p1,p2,dist])

    min1 = new_list[0][2]
    pair1 = 0
    for j in range(len(new_list)):
        # If the other element is smaller than first element
        if new_list[j][2] < min1:
            min1 = new_list[j][2] #It will change
            a = new_list[j][0]
            b = new_list[j][1]
            pair1 = a,b
    return [pair1,min1]
    pass

#############################################
# Problem 4
#############################################
class Vector2D:
    def __init__(self, *x):
        if x:
            self.tuple_value = x
        else:
            self.tuple_value = (0,0)

    def get_tuple(self):
        return self.tuple_value

    def __mul__(self, other):
        """
        mutiple self and other
        """
        a = self.get_tuple()[0]
        b = self.get_tuple()[1]
        c = other.get_tuple()[0]
        d = other.get_tuple()[1]
        return a * c + b * d
        pass

    def __add__(self, other):
        """
        add self and other
        """
        a = self.get_tuple()[0]
        b = self.get_tuple()[1]
        c = other.get_tuple()[0]
        d = other.get_tuple()[1]
        return a + c, b + d
        pass

    def __sub__(self, other):
        """
        TODO:
        Implement function described in the homework PDF
        """
        a = self.get_tuple()[0]
        b = self.get_tuple()[1]
        c = other.get_tuple()[0]
        d = other.get_tuple()[1]
        return a - c, b - d
        pass

    def __abs__(self):
        """
        TODO:
        Implement function described in the homework PDF
        """
        a = self.get_tuple()[0]
        b = self.get_tuple()[1]
        return math.sqrt(a**2 + b**2)
        pass

    def scalar_mul(self, x):
        """
        TODO:
        Implement function described in the homework PDF
        """
        a = self.get_tuple()[0] * x
        b = self.get_tuple()[1] * x
        self.tuple_value = a,b
        return self
        pass

    def __neg__(self):
        """
        TODO:
        Implement function described in the homework PDF
        """
        a = self.get_tuple()[0]
        b = self.get_tuple()[1]
        a = -1 * a
        b = -1 * b
        self.tuple_value = a,b
        return self
        pass

    def __eq__(self, other):
        """
        TODO:
        Implement function described in the homework PDF
        """
        a = self.get_tuple()[0]
        b = self.get_tuple()[1]
        c = other.get_tuple()[0]
        d = other.get_tuple()[1]
        if a == c and b == d:
            return True
        else:
            return False
        pass

    def __str__(self):
        return "{0}".format(self.get_tuple())


#############################################
# Main
#############################################
if __name__ == "__main__": 
    """

    """
    # Problem 1
    print()
    print("*"*30)
    print("* Problem 1")
    print("*"*30)
    x = [0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,1,1,0]
    print(lr(x))



    # Problem 2
    print()
    print("*"*30)
    print("* Problem 2")
    print("*"*30)
    x = [1,2,3,4,5,6,7,8,9,10]
    y = 5
    z = 3

    print(x,y,z)
    print(nn(x,y,z))

    # Problem 3
    print()
    print("*"*30)
    print("* Problem 3")
    print("*"*30)


    x = [(rn.randint(1,50), rn.randint(1,50)) for _ in range(10)]
    print("x", x)
    print("Distance between x[0] and x[1]: ", distance(x[0], x[1]))
    print("Brute:", brute(x))

    # Problem 4 
    print()
    print("*"*30)
    print("* Problem 4")
    print("*"*30)
    x = Vector2D(1,2)
    y = Vector2D(4,-1)
    w = Vector2D(1,2)
    print("Addition: ", x + y)
    print("Multiplication: ", x * y)
    print("Subtraction: ", x - y)
    print("Absolute value: ", abs(x))
    x.scalar_mul(5)
    print("Scalar Multiplication: ", x)
    -x
    print("Negative (1st): ", x)
    -x
    print("Negative (2nd): ", x)
    print("Equivalence: ", x == w)


