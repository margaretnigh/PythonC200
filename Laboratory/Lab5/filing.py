import os

def getCurrentDirectory():
    """
    This uses a command built into the python module `os` 
    that shows the current working directory. 

    Returns:
        A string that shows the current working directory 
        (Where the program is being executed at)
    """
    return os.getcwd()


def ourPrint(aString):
    """
    Prints the string in a way to easily represent the end of a file
    """
    print("~"*30)
    print(aString, end="") # end= removes the \n automatically added
    print("*EOF*")

def readingEx1():
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    with open("Laboratory/Lab5/blank.txt", "r") as someFile:
        someFile = open("Laboratory/Lab5/blank.txt", "r")
        contents = someFile.read()
        ourPrint(contents)

    pass


def readingEx2():
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    with open("Laboratory/Lab5/blank.txt", "r") as someFile:
        open("Laboratory/Lab5/blank.txt", "r")
        contents = someFile.readlines()
        ourPrint(contents)
    pass


def writeEx1():
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    stuff = ["a", "b", "c", "d", "e", "f"]
    with open("Laboratory/right.txt", "w") as fileToWrite:
        for s in stuff:
            fileToWrite.write(s)
            fileToWrite.write(s + "\n")
    pass


def writeEx2():
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    with open("Laboratory/Lab5/wrong.txt", "a") as fileToWrite:
        for s in range(4):
            fileToWrite.write("more\n")
    pass



def StripLab(filePath, newFile): 
    '''
    Given a file path, we want to open the file, read each line and count
    the number of lines that have "Laboratory" on them. We will write to 
    the newFile the lines that don't have "Laboratory" and clean them up 
    (use strip). You are provided the path to the file we want to write.
    
    Return number of lines with count. 
    '''
    count = 0

    with open(filePath) as theFile:
        originalContents = theFile.read()

    splitted = originalContents.split("\n")

    goodLines = []
    #count lines
    for line in splitted:
        if "Laboratory" in line.strip():
            count += 1
        else:
            goodLines.append(line.strip())

    #write lines
    with open(newFile, "w") as toWrite:
        for line in goodLines:
            toWrite.write(line)
            toWrite.write("\n")
        return count
    pass






if __name__ == "__main__":
    print()
    print("Examples of Reading")
    print("Our current working directory: " + getCurrentDirectory())
    print()
    print("Reading")
    readingEx1()
    print("-" * 20)
    readingEx2()
    print("-" * 20)
    print()
    print("Writing")
    print("-" * 20)
    writeEx1()
    writeEx2()
    print()
    print("Strip Lab Result: " + str(StripLab("Laboratory/Lab5/testing.data", "Laboratory/Lab5/clean.txt")))
