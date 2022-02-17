import math


###########################################################################
# Functions for Problem 1
###########################################################################

# This function will return a tuple of 2 values
# The "plus" value must be first in the tuple
# The "minus" value must be second in the tuple 
# The unit test expects ((v+u),(v-u)) **not** ((v-u),(v+u))
def q(a,b,c):
    """
    Input: a,b,c number ints
    Return: tuple of solutions
    recall ax**2 + bx + c = 0 
    """
    #discriminant
    dis = (b**2) - (4*a*c)
    sqrt_val = math.sqrt(abs(dis))  
    if dis < 0:
        #solution is complex
        comp = math.sqrt(-1 * dis) / (2*a)
        real = (-1*b) / (2*a)
        x1 = complex(real,comp)
        x2 = complex(real,-1*comp)
    else:
        #solution not complex
        #positive
        x1 = (-b + math.sqrt(dis)) / (2*a)
        #negative 
        x2 = (-b - math.sqrt(dis)) / (2*a)
     
    return ((x1,x2))
    pass



###########################################################################
# Functions for Problem 2
###########################################################################
def checkout(xlst):
    """
    Input: list of items [[x,y,z],...]
    Return: total cost of items
    """
    total = 0
    amt = 0
    tax = 1.07
    total_taxed = 0
    total_untaxed = 0
    for i in range(len(xlst)):
        item = xlst[i]
        num = item[0]
        price = item[1]
        taxable = item[2]
        amt = (num * price)
        if taxable == 1:
            #tax on item list
            total_taxed += amt
        else:
            total_untaxed += amt
    total_taxed = total_taxed * tax
    total = total_taxed + total_untaxed
    return(total)
    pass


###########################################################################
# Functions for Problem 3
###########################################################################
def open_seat_count(xlst):
    """
    Input: list of seats ex. [[1,0,0],[1,1,1],[1,1,0]]
    Output: number of open seats (0s)
    """
    seats_avail = 0
    for i in range(len(xlst)):
        row = xlst[i]
        for j in range(len(row)):
            if row[j] == 0:
                seats_avail += 1
    return seats_avail
    pass

###########################################################################
# Functions for Problem 4
###########################################################################
#INPUT List of numbers
#RETURN Various means or error message

def arithmetic_mean(nlst):
    """
    Input: list of nums
    Output: means or error
    """
    total = 0
    n = len(nlst)
    for i in range(len(nlst)):
        total += nlst[i]
    total = total / n
    if nlst == []:
        return "Data Error: 0 values"
    else:
        return total
    pass

def geo_mean(nlst):
    """
    Input: list of nums
    Output: means or error
    """
    a = 10
    n = len(nlst)
    sum = 0
    for i in range(len(nlst)):
        sum += math.log10(nlst[i])
    mean = math.pow(a,(sum/n))
    if nlst == []:
        return "Data Error: 0 values"
    else:
        return mean
    pass

def har_mean(nlst):
    """
    Input: list of nums
    Output: means or error
    """
    n = len(nlst)
    total = 0
    for i in range(len(nlst)):
        if nlst[i] == 0:
            return "Data Error: 0 in data" 
        total += 1 / nlst[i]
    total = n / total
    if nlst == []:
        return "Data Error: 0 values"
    else:
        return total
    pass

def RMS_mean(nlst):
    """
    Input: list of nums
    Output: means or error
    """
    n = len(nlst)
    total = 0
    for i in range(len(nlst)):
        total += (nlst[i]) ** 2
    total = math.sqrt(total/n)
    if nlst == []:
        return "Data Error: 0 values"
    else:
        return total
    pass


###########################################################################
# Functions for Problem 5
###########################################################################

#INPUT ISBN string, assume "D-DDD-DDDDD-D" 
# D is digit
#RETURN Boolean if valid ISBN
def valid_ISBN(ISBN_str):
    """
    INPUT: ISBN string, assume "D-DDD-DDDDD-D" 
    RETURN: Boolean if valid ISBN
    ISBN is a string “D-DDD-DDDDD-D” where D is a digit 0 through 9
    """
    #calculate 10 times the first digit, 
    # plus 9 times the second digit, 
    # plus 8 times the third digit and so on until we add 1 time the last digit. If the final number leaves no remainder when divided by 11, the code is a valid ISBN.
    #remove dashes
    ISBN_str = ISBN_str.replace("-","")
    #list of ISBNs
    ISBN_list = list(ISBN_str)
    num = 0
    total = 0
    #The digit is multiplied by its (location + 1) in the string (ignore the dashes)
    for i in range(len(ISBN_list)):
        ISBN_list[i] = int(ISBN_list[i])
        num = i + 1
        total += num * ISBN_list[i]
    if total % 11 == 0:
        return True
    else:
        return False
    pass


if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.
    You **do not** have to put anything here
    """
    pass