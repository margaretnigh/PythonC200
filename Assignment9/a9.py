
###############
# PROBLEM ONE
###############
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
import math


def get_data(path,name):
    tmp = []
    pn = os.path.join(path, name)
    file = open(pn, "r")
    for d in file:
        x,y = d.split(",")
        tmp += [[int(x), int(y)]]
    return tmp
    

def pop(year):
    """
    Input: years as in 1999 or 2003
    Output: population at that year theoretically
    uses given function
    """
    model_val = 1436.53*(pow(1.01395,year))
    return model_val
    pass

def error(data):
    """
    go through each year and compare to model
    Input: data as list populations
    Output: avg relative error
    """
    avg = 0
    for i in range(len(data)):
        year_pop = data[i]
        year = year_pop[0]
        pop_actual = year_pop[1]
        diff = abs(pop_actual - pop(year))
        #find total average relative error
        avg += diff / pop_actual
    avg = avg * (100/len(data))
    return avg

    pass



if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a9.py`. Feel free to add print statements. 
    """

    data = get_data("./Assignment9/", "pop.txt")
    print(data)
    total_error = round(error(data),4)
    t = np.arange(0.0, 120.0)
    fig,ax = plt.subplots()

    ax.plot(t, pop(t),'g')
    for y,p in data:
        ax.plot(y,p,'ro--')

    ax.set(xlabel ="Time (Year + 1900)", ylabel=r"Pop size $\times 10^6$",
    title = "Population Growth. Total ave error = %{0}".format(total_error))
    ax.grid()
    plt.show()

###############
# PROBLEM TWO
###############
import csv

def my_int(xstr):
    if xstr == "":
        return 0
    else:
        return int(xstr)
        
#INPUT state and state dictionary of data
#RETURN give the total confirmed deaths for 
# entire state
def scd(state,dic):
    """
    INPUT state and state dictionary of data
    RETURN give the total confirmed deaths for entire state int
    Process: creates total amt of confirmed deaths per state from data
    """
    total = 0
    #dic = {(“state”,“county”):[confirmed_cases, confirmed_deaths]}
    for key, value in dic.items():
        if key[0] == state:
            total += value[1] # total confirmed deaths
    return total
    pass  

#INPUT dictionary data and interval (a,b)
#RETURN all confirmed county cases greater than or equal to a
#and strictly less than b
#return a dictionary with state as key
def ccc(dic,interval):
    """
    INPUT dictionary data and interval (a,b)
    RETURN all confirmed county cases greater than or equal to a and strictly less than b (dictionary)
    Process: finds confirmed cases within an interval and prints the state and county
    """
    #dic = {(“state”,“county”):[confirmed_cases, confirmed_deaths]}
    #Additionally it adds an entry (a; b): number of state-counties
    confirmed = {}
    amt = 0
    a = interval[0]
    b = interval[1]
    for key, value in dic.items():
        if value[0] >= a and value[0] < b:
            confirmed[key[0],key[1]] = value[0]
            amt += 1
    confirmed[interval] = amt
    return confirmed
    pass

#INPUT state, data dictionary, state population
#RETURN state death density: confirmed deaths / population of state
#as a percentage to 3 places use round(x*100,3)
def sdd(state, dic, state_pop):
    """
    INPUT state, data dictionary, state population
    RETURN state death density: confirmed deaths / population of state as a percentage to 3 places use round(x*100,3)
    Process: find the death density at a certain state
    """
    pop = 0
    deaths = scd(state,dic) # int
    state_pop = state_pop[state]
    #get last population
    population = state_pop[len(state_pop)-1]
    density = deaths / population
    density = round(density*100,3)
    return density
    pass

#INPUT data dictionary and state population 
#RETURN return the entire US death density
def usdd(dic,state_pop):
    """
    INPUT data dictionary and state population 
    RETURN return the entire US death density
    Process: go through and compare death amt to pop = density
    """
    dict = {}
    #returns a dictionary with state as the key and death density as the value.
    for key in dic.items():
        state = key[0][0]
        if state == "Guam" or state == "Northern Mariana Islands" or state == "Virgin Islands":
            dict[state] = "Unknown"
        else:
            death_density = sdd(state,dic,state_pop)
            dict[state] = death_density
    return dict
    pass

def get_dic(file_path):
    """
    Reading from the file passed in, 
    extract the following information into a dictionary and RETURN a dictionary. 

    The key for the dictionary (also described in the document): a tuple
    The value for each key (also described in the document): a list of size 2 (both need to be integers)

    """
    #dic = {(“state”,“county”):[confirmed_cases, confirmed_deaths]}
    dict = {}
    with open('./Assignment9/' + file_path, newline='') as csvfile:
        reader = csv.reader(csvfile) #read the text
        next(reader, None) #skip first line
        for row in reader:
            state = row[2]
            county = row[1]
            confirmed_cases = row[6]
            confirmed_deaths = row[7]
            if confirmed_cases.isdigit():
                confirmed_cases = int(confirmed_cases)
            elif confirmed_cases == '':
                confirmed_cases = 0
            if confirmed_deaths.isdigit():
                confirmed_deaths = int(confirmed_deaths)
            elif confirmed_deaths == '':
                confirmed_deaths = 0
        
            dict[state,county] = [confirmed_cases, confirmed_deaths]
        csvfile.close()
    return dict
    
    pass

def get_state_pop(file_path):
    """
    Reading from the file passed in, 
    extract the following information into a dictionary and RETURN a dictionary. 

    The key for the dictionary (also described in the document): a string
    The value for each key (also described in the document): an integer

    To read the file, you can do it the way we have seen before or using csv.reader. https://docs.python.org/3/library/csv.html#csv.reader 
    If you want to do it another way, please ask before attempting to use a method not talked about in class.
    """
    #state_pop = {“state”:population”}
    temp = []
    dict = {}
    with open('./Assignment9/' + file_path, newline='') as csvfile:
        reader = csv.reader(csvfile) #read the text
        for row in reader:
            temp.append(row)
        for i in range(len(temp)-1):
            state = temp[i][0]
            population = temp[i][1:]
            for k in range(len(population)):
                if population[k].isdigit():
                    population[k] = int(population[k])
                elif population[k] == '':
                    population[k] = 0
            dict[state] = population
        csvfile.close()
    return dict      
    pass



if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a9.py`. Feel free to add print statements. 
    # """

    #Our solutions used these two dictionaries 
    # has state, county, confirmed case, comfirmed deaths 
    # has state *most* current population 
    dic = get_dic("us-counties.csv")
    state_pop = get_state_pop("sp.csv")
    print(state_pop)
    
    #county confirmed cases
    intervals = [(0,1),(1,2),(0,2)]
    c0 = ccc(dic,intervals[0])
    c1 = ccc(dic,intervals[1])
    c2 = ccc(dic,intervals[2])
    if c0:
        print(f"Number of state-counties {intervals[0]} is {c0[intervals[0]]}")
    if c1:
        print(f"Number of state-counties {intervals[1]} is {c1[intervals[1]]}")
    if c2:
        print(f"Number of state-counties {intervals[2]} is {c2[intervals[2]]}")
    max = float('inf')
    cm = ccc(dic,(266380,max))
    print(">= 266380 confirmed cases")
    print(cm)

    #state confirmed deaths
    print(f"Alabama: {scd('Alabama', dic)}")
    if state_pop:
        print(f"Alabama state pop: {state_pop['Alabama']}")
    print(f"Alabama death density: {sdd('Alabama', dic, state_pop)}%")
    print(f"{round((8166 / 4903185)*100, 3)}%")

    #entire country death density percentage
    x = usdd(dic,state_pop)
    if x:
        print(f"Alabama: {x['Alabama']}%")
        print(x["Texas"])

###############
# PROBLEM THREE
###############
import math 
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

"""
simpson takes a function,beginning and ending points a and b, and the number of intervals
 over which to estimate the integration

 for example, we might define a function

 def some_function(x): 
     return 3*x*x + 1

 and estimate the integral from 0 to 6 with 100 steps

 simpson(some_function,0,6,100)
 """

def simpson(fn,a,b,n):
    """
    Input: fn = function parabola, a = float num point start, b = float num point end, n = interval int
    Output: area of function between two points
    Process: look between a and b points, keep intervals and add to list. sum of list is area
    """
    temp = [fn(a)]
    change_in_x = (b - a)/n
    fnx = 0
    a12 = (b - a)/(3*n)
 
    for i in range(1,n):
        xi = a + i * change_in_x #equation (8)
        if i % 2 == 0: #len(tmp) = 1
            fnx = fn(xi) * 2
            temp += [fnx]
        else:
            fnx = fn(xi) * 4
            temp += [fnx]
   
    temp += [fn(b)]
    sum1 = sum(temp) * a12
    return sum1


if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a9.py`. Feel free to add print statements. 
    """

    data = [[lambda x:3*(x**2)+1, 0,6,2],[lambda x:x**2,0,5,6],[lambda x:math.sin(x), 0,math.pi, 4],[lambda x:1/x, 1, 11, 6]]

    for d in data:
        f,a,b,n = d
        print(simpson(f,a,b,n))

    t = np.arange(0.0, 10.0,.1)
    fig,ax = plt.subplots()
    s = np.arange(0,6.1,.1)
    ax.plot(t, (lambda t: 3*(t**2) + 1)(t),'g')
    plt.fill_between(s,(lambda t: 3*(t**2) + 1)(s)) 
    ax.grid()
    ax.set(xlabel ="x", ylabel=r"$f(x)=3x^2 + 1$",
    title = r"Area under the curve $\int_0^6\,f(x)$")

    plt.show()