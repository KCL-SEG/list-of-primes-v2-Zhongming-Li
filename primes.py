"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if (number_of_primes == 0 or number_of_primes < 0):
        raise ValueError("The number of primes must be a positive integer")
    list = []
    current_num = 2
    while (len(list) < number_of_primes):
        for i in range (2, current_num+1):
            if (i == current_num):
                list.append(current_num)
            elif (current_num % i == 0):
                break
        current_num += 1

    return list
