"""
    Find the sum of the multiples of 3 and 5 up to 1000.
"""

if __name__ == "__main__":
    # Sum multiples up to N
    N = 1000

    # Brute force
    s = 0
    for i in range(N):
        if i % 3 == 0 or i % 5 == 0:
            s += i

    # Another solution, by Project Euler (slightly modified for deeper understanding):
    def triangular(n):
        return (n * (n + 1)) // 2

    def sum_of_multiples(m, n):
        return m * triangular(n // m)

    pe_s = sum_of_multiples(3, N - 1) + sum_of_multiples(5, N - 1) - sum_of_multiples(15, N - 1)

    assert (s == pe_s)
    s = pe_s

    print(s)
