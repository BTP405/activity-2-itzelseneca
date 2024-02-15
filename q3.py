def wordCount(t):
    """
    This function retrives data in a text file and returns a dictionary where the keys are unique words in the files and 
    the corresponding values are lists of line numbers where the words are found in the text.

    Parameters:
    (t): The text file to retrieve data from

    Returns:
    myDictionary: A dictionary that holds true if number is prime, false otherwise.
    """
    myDictionary = {}
    lineNum = 0
        
    with open(t, 'r') as file: # open file t in read mode (with: handles closing file for us)
        for line in file:     
            lineNum += 1 # increment line number counter for this new line
            words = line.strip().split() # remove leading and trailing white spaces, split words in line ['how', 'are', 'you']
            for word in words:
                if word not in myDictionary: # if WORD isnt a key in the DICTIONARY, add it with an empty list as value
                    myDictionary[word] = []
                if lineNum not in myDictionary[word]: # if current LINE number is not already in the LIST of the word, append it
                    myDictionary[word].append(lineNum)
    
    return myDictionary

print(wordCount('q3.txt'))