def statDecorator(func):
    """
    This function is a decorator that prints the numbers read, the count of the numbers read, the average of the numbers, the maximum of the numbers

    Parameters:
    (func): The function that will be decorated

    Returns:
    wrapper: A function that prints the line statistics
    """
    def wrapper(t):
        fileLines = func(t)  # run function passed as parameter to get the list of nums for every line[[10,50,40], [30,15],..]
        for line in fileLines:
            numList = [int(num) for num in line.split()]  # use comprehension to generate the list of nums for the current line [10,50,40]
            # printing stats for the current line
            print("Numbers read:", numList)
            print("Count of numbers read:", len(numList))
            print("Average of numbers:", sum(numList) / len(numList))
            print("Maximum number:", max(numList), "\n")
    return wrapper

@statDecorator
def printStats(t):
    """
    This function retrives data in a text file t which reads in lines of numbers, for each line read in,
    this function will call a decorator function statDecorator which prints line information

    Parameters:
    (t): The text file to retrieve data from

    Returns:
    fileLines: A list containing all lines in the file [[10,50,40], [30,15],..]
    """
 
    with open(t, 'r') as file: # open file t in read mode (with: handles closing file for us)  
        fileLines = file.readlines() # get file lines
    return fileLines

printStats("q4.txt")