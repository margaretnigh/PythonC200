"""
One of the code implementations for the problems in Lab3.py

I may add some more interesting functions such as append_prime_number
"""
# List Operations

def manual_append(list_one, element):
    '''
    given a list and an element append the element to the list 
    note to do this operation you can't use the .append method for lists

    inputs:
    list_one - a list of values can be any type
    element - a value of any type

    output:
    one coherent list of all elements combined

    '''
    combined_list = list_one + [element]
    return combined_list

    pass

def manual_remove(list_one, val):
    '''
    given a list and a specific value remove the item and report wether you were successful 
    by using a for loop to iterate over the list

    inputs:
    list_one - list of specific type(int or str) 
    val - the value that you want removed

    output:
    list - the list with the element removed if the element is not found return the list
    '''
    new1_list = []
    for index in range(len(list_one)):
        #0 to length of list
        if list_one[index] == val:
            #remove val dont put value in new list
            if not(list_one[index] == val):
                manual_append(new1_list, list_one[index])
    return new1_list
    pass

# Doing things with list data structures

def compare_lists(list_one, list_two):
    '''
    given 2 lists compare and report which indexes are different in an output list

    your output should look something like this: [1, 3, 5]
    
    which means that index 1, 3, and 5 are different values these lists can compare any data type

    inputs:
    list_one - list of a specific type (int or str) of length n
    list_two - list of a specific type (int or str) of length n

    outputs:
    list of ints which correlate to indexes that are different in a list
    '''
    new_list2 = []
    for i in range(len(list_one)):
        for j in range(len(list_two)):
            if i == j:
                if list_one[i] == list_two[j]:
                    pass
                else:
                   manual_append(new_list2,i) 

    return new_list2
    pass

def factorial_for(n):
    '''
    given a number calculate the factorial value using a for loop

    input:
    n - integer value that will be factorial you want to calculate 

    output:
    the calculated factorial of the input value 
    '''
    factorial = 1
    for i in range(1, 0, n+1):
        factorial = factorial * i
    return factorial
    pass


if __name__ == '__main__':
    # TODO:
    # implement testing
    pass
    
    
