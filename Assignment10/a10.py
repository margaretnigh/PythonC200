import random as rn
import math

#############################################
# Problem 1
#############################################
def sel_sqrt(a,b):
    """
    Input: a,b ints
    Output: list
    Process: list containing the integers i between a and b: 
    the square root of i if i is odd, and 2*i if i is even 
    using list comprehension
    """
    sel = [(2*i) if i%2==0 else round(math.sqrt(i),2) for i in range(a,b+1)]
    return sel

def inchtomtuple_lc(hlist_in):
    """
    Input: list of hights in inches
    Return: list of tuples
    Process: where the first element in each tuple is a height in inches, 
            second element of the tuple is the height in meters.
    ONLY List Comprehension
    """
    #convert
        #0.0254 meters per inch. 
        #Be sure to round the height in meters to 4 decimal places.
    meters = [round(i*0.0254,4) for i in range(len(hlist_in))]
    #format
    tup = [(hlist_in[i],meters[i]) for i in range(len(hlist_in))]
    return tup

def intomtuple_map(hlist_in):
    """
    Input: list of hights in inches
    Return: list of tuples
    Process: where the first element in each tuple is a height in inches, 
            second element of the tuple is the height in meters.
    ONLY Map and Lambda
    """
    meters = map(lambda x: round(x*0.0254,4), hlist_in)
    tup = map(lambda x, y: (x,y), hlist_in, meters)
    return list(tup)
    pass

#############################################
# Problem 2
#############################################
def bmi_calc(weight, height):
    """
    Input: the weight and height of a person
    Returns: their BMI
    """
    return round(703 * (weight/height**2),2)
    pass
    
def bmi_lc(blist):
    """
    """
    return [(bmi_calc(x[0],x[1])) for x in blist]
    pass

def bmi_map(blist):
    return list(map(lambda x: bmi_calc(x[0],x[1]), blist))
    pass

def bmi_cat(bmilist):
    """
    underweight - less than 18.5
    normal - greater than or equal to 18.5 and less than 25
    overweight - greater than or equal to 25 and less than 30
    obese - greater than or equal to 30
    """
    return [((i,'underweight') if i < 18.5 else ((i,'normal') if i >= 18.5 and i < 25 else(((i,'overweight')) if i >= 25 and i < 30 else(((i,"obese")) if i > 30 else i)))) for i in bmilist]

#############################################
# Problem 3
#############################################
def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1],a[j]

    return a

def wbubble_sort(a):
    """
    ONLY while loops
    """
    x = 0
    #loop through list
    while x < len(a)-1:
        #swap
        while a[x] > a[x+1] and x >= 0:   
            a[x], a[x+1] = a[x+1],a[x]
            if x != 0:
                x = x - 1
        x = x + 1
    return a

#############################################
# Problem 4
#############################################
def rsel_sort(xlst):
    """
    Input: list of numbers as an input argument
    Process: selection sort uses the original list and creates a
    new sorted list. It finds the smallest number in the original list, adds it to the end of the sorted list,
    and removes this number from the original list
    min,remove allowed
    """
    minimum = 0
    if xlst == []:
        return xlst
    else:
        minimum = min(xlst)
        xlst.remove(minimum)
        return [minimum] + rsel_sort(xlst)
    

#############################################
# Main
#############################################
if __name__ == "__main__": 
    # Problem 1a
    print("sel_sqrt")
    print(sel_sqrt(0,10))
    print(sel_sqrt(10,15))
    print(sel_sqrt(15,20),"\n")

    # Problem 1
    print("Heights")
    heights = []

    for i in range(10):
        heights.append(rn.randint(48,90))
    print(heights)

    print(inchtomtuple_lc(heights))
    print(intomtuple_map(heights),"\n")

    # Problem 2
    print("BMI")
    wh = []
    for i in range(10):
        wh.append((rn.randint(100, 300), heights[i]))
    print(wh)

    print("bmi LC: ", bmi_lc(wh))
    print("bmi Map: ", bmi_map(wh))
    print("bmi Cat: ", bmi_cat(bmi_map(wh)))

    # Problem 3 
    print("Bubble Sort") 
    test = []

    for i in range(10):
        test.append(rn.randint(0,100))
    print("test", test)

    print(bubble_sort(test))
    print(wbubble_sort(test))

    # Problem 4
    print("Selection Sort")
    test = []

    for i in range(10):
        test.append(rn.randint(0,100))
    print(test)
    print(rsel_sort(test))