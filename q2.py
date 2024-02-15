import matplotlib.pyplot as plt

def graphSnowfall(t):
    """
    This function retrives data in a text file t and displays that information in a bar chart.
    The file will have a single number on each line representing the amount of snowfall accumulation for a given day. 
    Aggregate these values so that each one contributes to a particular 10 cm range. 

    Parameters:
    (t): The file to retrieve the data from 

    Returns:
    graph.png: A png which showcases the bar chart
    """

    with open(t, 'r') as file: # open file t in read mode (with: handles closing file for us)  
        fileLines = file.readlines() # get file lines

        x = ["0-10", "11-20", "21-30", "31-40", "41-50"] # initialize x axis 
        y = [0, 0, 0, 0, 0]  # initialize y axis 

        for num in fileLines: # for the number in the current line,
            y[((int(num)-1)//10)] += 1 # to get y index: subtract 1 from num to offset, floor division by 10. then increase counter at found index

    plt.bar(x, y) # creating graph

    # labeling
    plt.title("Accumulated Snowfall")
    plt.xlabel("Snowfall range(cm)")
    plt.ylabel("No. of occurences")

    plt.savefig("graph.png") # export graph

graphSnowfall("q2.txt")