import random as rn
import numpy as np

"""
Problem 1
"""
def unique_words(xstring):
    """Problem 1.  Find the unique words in a string

    Args: a string input

    Returns: a unique list of each word once

    """
    unique = []
    #get rid of the periods
    xstring = xstring.replace(".", " ")
    xstring = xstring.replace(",", "")
    #covert to all lowercase
    string = xstring.lower()
    #split into a list
    string = string.split()
    for i in string:
        if i not in unique:
            unique.append(i)
    return unique
    pass

def get_transition_matrix(xtr):
    """Problem 1.  Generate the transition matrix
    Goal: count of the number of times a certain word transition occurs
    Info:
        -rows indicate the first word in the transition
        -columns define the second word in the transition
        -The number at the intersection of each row and columns indicates how many times that word transition occurred in the text
    Args: string input
    Returns: transition matrix
    """
    unique = unique_words(xtr) # ex. ['the', 'cat', 'is', 'outside', 'but', 'should', 'be', 'in', 'house']
    #convert to find the real list of each word in og sentence
    string = xtr.replace(".", " ")
    string = string.replace(",", "")
    string = string.lower()
    string = string.split()

    matrix_temp = []
    matrix =[]
    pairs = []
    count = 0

    for i in range(len(string) - 1): #go through each word in the original string
        #pairs in original list
        pairs.append(str(string[i]) + " " + str(string[i+1])) #pairs in the string

    #find all the pairs
    for row in range(len(unique)):
        for col in range(len(unique)):
            pair = str(unique[row]) + " " + str(unique[col]) #each pair possible
            if pair in pairs:
                while pair in pairs:
                    count += 1
                    pairs.remove(pair)

            else:
                count = 0
            matrix_temp.append(count)
    for x in range(0,len(matrix_temp),len(unique)):
        line = matrix_temp[x:x+len(unique)]
        matrix.append(line)

    return matrix
  


"""
Problem 2
"""
def running_average(xlist,per):
    """Problem 2.  Compute the running average

    Args: 
        receives an arbitrary length list of numbers
        number indicating the period for computing the running average

    Returns:
        a list that contains the running average based on that period

    """
    averages = []
    values = []
    average = 0
    for i in range(len(xlist)):
        #i represents the day
        #[i] represents the number at that day
        values = xlist[i:i+per]
        if len(values) == per:
            for j in range(len(values)):
                average += values[j]
            average = average / per
            average = round(average,2)
            averages.append(average)
            average = 0
    return averages
    pass


##########################################################################
if __name__ == "__main__":
    # Fill in with code to test your functions for both problems
    # Note that the np.array() function converts the list that is returned to 
    # a numpy array. This is only done for display/print purposes, so be sure that
    # your function returns a list.
    text1 = "The cat is outside, but the cat should be in the house."
    text2 = "The cat is in the house. The dog is outside playing with the ... kids. Both the dog and the cat need a bath. The kids need to ...come in and eat dinner."
    uniwords = unique_words(text1)
    print(uniwords)
    print("There are {0} unique words in the text.".format(len(uniwords)))
    

    print("The Transition Matrix is Below:")
    #np.array() converts the list to a numpy array for display/print purposes.
    print(np.array(get_transition_matrix(text1)))

    #Generate random data sequence
    data = [11, 82, 91, 55, 32, 91, 12, 5]
    print(data)
    period = 3 # time period for running avg (3 day average)
    run_avg = running_average(data,period)
    print("The {0}-day running average is: {1}".format(period,run_avg))