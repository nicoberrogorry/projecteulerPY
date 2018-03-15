"""
    Find the sum of even Fibonacci terms which are smaller than four million.
"""

import collections

if __name__ == "__main__":
    # Brute force approach
    prevFib = 1
    # 1 is NOT even -> efsum = 0

    fib = 2
    # 2 is even -> efsum += 2
    evenFibSum += fib

    # Calculate, compare and sum the next terms before four million
    while fib < 4000000:
        if fib % 2 == 0:
            evenFibSum += next_fib
        backupFib = fib
        fib += prevFib
        prevFib = fib

    print("Brute: {}".format(evenFibSum))


    # More efficient approach
    '''
        Introduction:
            The sum of an odd number and an even number is odd.
        Its trivial to prove the sum of two odd numbers is an even number.
        
        f(1) = 1 -> odd
        f(2) = 1 -> odd
        f(3) = 1 + 1 = 2 -> even
        f(4) = 2 + 3 = 5 -> odd
        f(5) = 5 + 2 = 7 -> odd
        f(6) = 5 + 7 = 12 ->even

        Looks like every third term is even...
        
        Fibonacci's sequence closed form:
        f(n) = (pow(1 + sqrt(5), n) - pow(1 - sqrt(5), n)) / sqrt(5)
        
        So every third term's closed form is:
        f(3n) = (pow(1 + sqrt(5), 3n) - pow(1 - sqrt(5), 3n)) / sqrt(5)

    '''
    sqrt5 = sqrt(5)
    gr = 1 + sqrt5
    ngr = 1 - sqrt5
    
    evenFibSum = 0
    k = 3
    fib = 2
    while fib < 4000000:
        fib = (pow(gr, k) - pow(ngr, k))
        evenFibSum = evenFibSum + fib
        k = k + 3
    evenFibSum = evenFibSum / sqrt5

    print("Efficient: {}".format())
