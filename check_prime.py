import math


def check_prime(n):
    """Method to check if number(n) is prime"""
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def check_prime_in_range(n):
    """
    Sieve of Eratosthenes
    Find prime numbers in a certain range(<=n)
    """
    array = [True for _ in range(n + 1)]
    for num in range(2, int(math.sqrt(n)) + 1):
        if array[num] == True:
            mul = 2
            while num * mul < n:
                array[num * mul] = False
                mul += 1
    for i in range(2, n + 1):
        if array[i]:
            print(i, end=" ")
