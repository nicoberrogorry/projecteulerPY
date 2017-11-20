"""
    Find the sum of even Fibonacci terms which are smaller than four million.
"""

import collections

if __name__ == "__main__":
    limit = 4000000

    # Brute force
    prev_fib = 1
    fib = 2

    '''
        Later we'll always test against the next Fibonacci terms before the limit, so we test and
        sum the first two terms manually:
            1 is NOT even -> s = 0
            2 IS even -> s += 2 -> s = 2
    '''
    s = 2

    # Work on the next pair of Fibonacci terms
    go_on = True
    while go_on:
        prev_fib += fib
        # Test limit
        if prev_fib < limit:
            # Test and sum
            if prev_fib % 2 == 0:
                s += prev_fib

            fib += prev_fib
            if fib % 2 == 0:
                s += fib
        else:
            # Limit hit
            go_on = False

    print("Brute force says: {}".format(s))

    # Yet another solution, by Project Euler
    '''
        Every third Fibonacci number can be calculated with a recursive function:

            g(n) = 4 * g(n-1) + g(n-2)

        Note: This proof can be obtained by proving f(n) = 4 * f (n-3) + f(n-6) for every nth
              Fibonacci term.
    '''
    def g(n, res=collections.Counter({'sum': 10, 'calls': 0}), gn__: int = None, gn_: int = None):
        res['calls'] += 1

        if gn__ is None or gn_ is None:
            if n == 3:
                gn__, gn_ = 2, 8
            else:
                _, gn__, gn_ = g(n - 1)

        gn = 4 * gn_ + gn__

        if gn < limit:
            res['sum'] += gn

        # The parent g(n) recycles the value g(n-1) and g(n), avoiding
        return res, gn_, gn

    g_res, _, _ = g(11)

    print("Recursive solution: {} with {} recursions".format(g_res['sum'], g_res['calls']))
