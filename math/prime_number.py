import math
import numpy as np

def main():
    print("Prime Number")

    print(f"11 is prime: {is_prime_naive(11)}")
    print(f"9 is prime: {is_prime_naive(9)}")
    print(f"997 is prime: {is_prime_naive(997)}")

    print(sieve_of_erastothenes(100))

# Either go till n or n/2
def is_prime_naive(num):
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    
    return True

# if a number is not prime the first factor will be within sqrt(num)
def is_prime_optimized(num):
    for i in range(2, math.floor(math.sqrt(num))+ 1):
        if num % i == 0:
            return False
    
    return True

"""
The More optimal soln is to use the idea as follows
Step 1: Check if num is 1, if so return false
Setp 2: Check if num is 2 or 3, return True
Step 3: Check if num is divisible by 2 or 3, return False
Step 4: Start i from 5 and go till i^2 < num, check if num is divisible by i or i+2, return False
Setp 5: Increment i by 6
"""
def is_prime(num):
    if num == 1:
        return False
    
    if num == 2 or num == 3:
        return True
    
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    i = 5

    while i * i <= num:
        if num % i == 0 or num % (i+2) == 0:
            return False
        i += 6

    return True
"""
Optimized Algorithm for printing prime numbers btw 1 to n

Step 1: Create a boolean array size = n, mark all values as false
Step 2: Start i from 2 loop till sqrt(n) if not marked in bool array(false):
Step 3: run another loop from i*i (first unmarked number will be the square) till n and mark all multiples
Step 4: print unmarked numbers
"""
def sieve_of_erastothenes(num):
    bool_array = [False] * num 

    i = 2

    while i * i <= num:
        if bool_array[i] == False:
            j = i * i
            while j < num:
                bool_array[j] = True
                j = j + i
        
        i += 1
    
    for i in range(2, num):
        if bool_array[i] == False:
            print(i)
    
# Application of above algorithm
def count_primes(self, n):
        """
        :type n: int
        :rtype: int
        """
    
        bool_array = [False] * n

        i = 2

        while i*i < n:
            if bool_array[i] ==  False:
                for j in range(i * i, n, i):
                    bool_array[j] = True
            
            i += 1
        
        count = 0

        for num in bool_array[2:]:
            if not num:
                count +=1

        return count

if __name__ == "__main__":
    main()