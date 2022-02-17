"""
    C200 Homework Assignment 6 : ppm modify

    Author: Margaret Nigh

    Date:   October 19th 2021

    The goal of this assignment is to give you practice working with lists
    by writing a program that manipulates image files in various ways.

    1. In a PPM file, if the second line of the header is 4 6, how many integer
    values will be there be the body of the PPM file? why?
        4 pixels wide and 6 pixels tall = 24 pixels in all, 72 integer values

    2. Given a line of RGB values 1 2 3 200 100 150 4 5 6, which of these
    values represent red?
        red=1 in 1,2,3. red = 200 in 200,100,150. red = 4 in 4,5,6

    3. A program can read the PPM file line by line. When a line is read, what
    process do you need to perform in order for you to access and manipulate
    the RGB values that are separated by whitespace (the ASCII whitespace
    characters include space, tab, linefeed, return, formfeed, and vertical tab
"""
import math
from math import sqrt  

def color_translate(line):
    """
    Input: a single line from ppm file str
    Goal: takes in a line (string) and translates it to an rgb value scale wanted
    Return: a string line of values each edited
    """
    numbers = line.split(" ")
    string = ""
    for digit in range(len(numbers)):
        value = numbers[digit]
        value = value.strip()

        if value.isdigit():
            value = int(value)
            if value % 3 == 0:
                value = 0
            elif value % 3 == 1:
                value = 153
            elif value % 3 == 3:
                value = 255
        value = str(value)
        string += value + " "
    return string
    pass

def process_ppm(in_filename, out_filename, filter):
    """
        Input: in_filename (ppm that already exists), out_filename (new ppm), filter (function grey or color)
        Process: The body of out_filename will be generated from the body of in_filename line-by-line using the processing function color_translate
        Return: output file new file written with filter applied
    """
    #open files
    input_ = open(in_filename, "r")
    output_ = open(out_filename, "w")

    lines = input_.readlines() #list: [line, line, line, ...] each line is a string
    output_.write(lines[0] + '\n') 
    output_.write(lines[1] + '\n') 
    output_.write(lines[2] + '\n') 
    lines = lines[3:] #get rid of the first 3 lines that are describing the doc
    for line in range(len(lines)): #go through to each line
        new_line = filter(lines[line]) # add filter to line
        #add new line to new ppm file
        output_.write(new_line + '\n')
    input_.close()
    output_.close()


def main_part1():
    # TODO: call the <decode> function you developed to decode
    #  the image <files/part1.ppm>
    # copies in_filename to out_filename
    process_ppm("Assignment6/files/part1.ppm", "Assignment6/files/part1_new.ppm", color_translate)
    process_ppm("Assignment6/files/luddy.ppm", "Assignment6/files/luddy_new.ppm", grey_scale)
    pass

def grey_scale(line):
    """ 
        Input: a single line from ppm file str
        Goal: convert to grey scale using the conversion
        Return: a string line of the values as grey scale
    """
    numbers = line.split(" ")
    string = ""
    nums = []
    for digit in range(len(numbers)):
        value = numbers[digit]
        value = value.strip()
        if value.isdigit():
            value = int(value)
            nums.append(value)
    for num in range(0,len(nums),3):
        #find red green blue
        temp = nums[num:num+3]
        r = temp[0]
        g = temp[1]
        b = temp[2]
        #value between 0 and 255 (inclusive), separated by whitespace
        grey = math.sqrt((r ** 2) + (g ** 2) + (b ** 2))
        grey = math.ceil(grey)
        #anything greater than 255 should be set equal to 255
        if grey > 225:
            grey = 225
            r = str(grey)
            g = str(grey)
            b = str(grey)
        else:
            r = str(grey)
            g = str(grey)
            b = str(grey)
        #add to str
        string += r + " " + g + " " + b + " " 
    return string
    pass

def main():
    """
    1. Ask the user for an input file.
    2. Ask the user for an output file.
    3. Perform grey_scale conversion on the input file and write the
       result to the output file in ppm format (don't forget to write out
       the header information!).
    4. WRite the complete docstring
    """
    in_file = input("Name the Input File: ")
    out_file = input("Name the Output File: ")
    grey_image = process_ppm("Assignment6/files/" + in_file, "Assignment6/files/" + out_file, grey_scale)
    pass


if __name__ == '__main__':
    main_part1()  # comment this out after you check-in for part 1
    #main()  # uncomment this after you check-in for part 1

