"""
Write a program to determine if a number, given on the command line, is prime.

    How can you optimize this program?
    Implement The Sieve of Eratosthenes, one of the oldest algorithms known (ca. 200 BC).
"""
import sys
def isPrime(*args):
    number = int(args[1])
    if(number <= 1): 
        return False
    if(number <= 3):
        return True
    # this could be slightly faster by checking the number is divisible by 2 or 3 first before running the while loop
    # all prime come in the form 6k ± 1
    i = 5
    while(i * i <= number):
        if(number % i == 0 or number % (i + 2) == 0) :
            return False
        i = i + 6

    return True
def sieve(*args):
    number = int(args[2])
    #creates the sieve for the size of the number of boolean 
    prime = [True for i in range(number + 1)]
    p = 2
    while (p * p <= number):
            # If prime[p] is true its prime
        if(prime[p] == True):
            for i in range(p * 2, number + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    for p in range(number + 1):
        if prime[p]:
                print(p)
                
if(sys.argv[1] == "true"):
    sieve(*sys.argv)
else:
    print(isPrime(*sys.argv))




