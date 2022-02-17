"""
    C200 Homework Assignment 6 : PPM Processing

    Name: Margaret Nigh

    Date:   WHEN YOU COMPLETED IT

    The goal of this assignment is to give you practice working with nested lists
    by writing a program that manipulates the entire image with multiple lines.
"""


def process(lines, rows, cols):
    """
    Input: 
        -lines is a list of strings representing the body of an image (already split)
        -rows is an int representing the number of rows
        -cols is an int representing the number of columns
    Return:
        -returns a list of lists ints
    
    The length of this list should be rows. 
    Each element of this list should be a list of length 3*cols representing
    the r, g, b values for all the pixels in a given row in the image.
    """
    list_digits = []
    temp = []
    temp2 = []
    #convert to integers
    for digit in range(len(lines)):
        value = lines[digit]
        if value.isdigit():
            value = int(value)
            list_digits.append(value)

    for num in range(0,len(list_digits),3):
        #find red green blue
        temp.append(list_digits[num:num+3])

    for rgb in range(0,len(temp), cols):
        temp2.append(temp[rgb:rgb+cols])
    return temp2
    pass


def read_ppm(filename):
    """
    Input: string as input file name
    Output: a list of strings representing the body of an image (split)
    Process: 
    """
    new_list = []
    filename = open(filename, "r")
    this_file = filename.read()
    this_file = this_file.replace("\n"," ")
    this_file = this_file.split(" ")
    for i in range(len(this_file)):
        if this_file[i] != '':
            new_list.append(this_file[i])
    filename.close()
    new_list = new_list[4:]
    return new_list
    pass


def write_ppm(image, filename):
    """
    Input:  inputs a list of lists of interger numbers and a string (filename)
    Output:
    Every int will have a value between 0 and 255 (inclusive); every sublist will have the same length
    Process: The function interprets this list of lists as an
    image and writes out a valid ppm file to an output file with name filename.
    """
    output_ = open(filename, "w")
    #write file info/header
    filename.write()
    filename.write()
    filename.write()
    for line in range(len(image)): #go through to each line
        output_.write(line + '\n')
    output_.close()
    pass


def scale(image, row_scale, col_scale):
    #check if a row of data will be kept in the scaling image
    """
    Input: 
        takes an image (a list of lists of ints, as returned by the process function)
         and two scaling factors, both ints. 
    Output: 
        is a list of list of ints.
    """
    #[[[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 255]],
    # [[0, 0, 0], [255, 0, 0], [0, 255, 0], [0, 0, 255]],
    # [[255, 0, 255], [0, 0, 0], [255, 0, 0], [0, 255, 0]],
    # [[0, 255, 255], [255, 0, 255], [0, 0, 0], [255, 0, 0]],
    # [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 255]],
    # [[0, 0, 0], [255, 0, 0], [0, 255, 0], [0, 0, 255]]]

    temp = []
    temp2 = []
    final = []
    for a in range(len(image)): #rows
        row = image[a]
        if a % col_scale == 0:
            temp.append(row) #row scale applied

    for b in range(len(temp)): #rows
        if b % row_scale == 0:
            temp2.append(temp)

    for j in range(len(temp2)):
        for k in range(len(temp2[j])):
            if k % 2 != 0:
                final.append(temp2[j][k])
        
    return final
    #scale(image, 3, 2) = [[255,0,0], [0,0,225]]
                        # [[0,255,255],[0,0,0]]
            
    pass

def main():
    #Ask the user for an input file name.
    input_ = input("What is your input file name?")
    #Ask the user for an output file name.
    output_ = input("What is your output file name?")
    #Ask the user for a height scaling factor.
    height_x = input("What is your height scaling factor?")
    height_x = int(height_x)
    while height_x < 0:
        height_x = input("What is your height scaling factor?")
    #Ask the user for a width scaling factor.
    width_x = input("What is your width scaling factor?")
    width_x = int(width_x)
    while width_x < 0:
        width_x = input("What is your height scaling factor?")
    #Process the image!
    #1.read
    read_image = read_ppm("Assignment6/files/" + input_)
    #2.process
    processed = process(read_image, 6, 4)
    #3.scale
    new_scale = scale(read_image, height_x, width_x)
    #4.write

    pass


if __name__ == '__main__':
    read_image = read_ppm("Assignment6/files/small.ppm")
    print(read_image)
    print(" ")
    processed = process(read_image, 6, 4)
    print(processed)
    print(" ")
    new_scale = scale(processed, 3, 2)
    print(new_scale)
    print(" ")
