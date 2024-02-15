def isPrime(n):
    """
    This function checks if the number passed is prime.

    Parameters:
    (n): The number to check 

    Returns:
    bool: A boolean that holds true if number is prime, false otherwise.
    """
    for i in range(2, n): # loop from 2 to (n - 1)
        if (n%i) == 0: # if dividing n by index/i has no remainder, n is not prime
            return False 
    return True 

def getPrimeNumbers(n):
    """
    This function uses helper function to determine if a number is prime and uses a comprehension to generate the list.

    Parameters:
    (n): The number to pass to helper function, upper limit of loop/list

    Returns:
    list: A list containing all prime numbers between 2 and n. 
    """
    return [num for num in range(2, n + 1) if isPrime(num)] # iterates over nums from 2 to n, checking if num is prime using the isPrime() function to generate list

print(getPrimeNumbers(19)) 