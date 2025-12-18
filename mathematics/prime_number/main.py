import math

def main():
    print("Check Prime Number")
    print("11 is prime", prime_efficient(11))
    print("10 is prime", prime_efficient(10))

def prime_number(n):
    if n <=1:
        return False
    
    x = math.sqrt(n)
    for i in range(2, x + 1):
        if n % i == 0:
            return False
    
    return True

def prime_efficient(n):
    if n == 1:
        return False
    
    if n == 2 or n == 3:
        return True
    
    if n%2 == 0 or n%3 == 0:
        return False
    
    i = 5

    while i*i <= n:
        if n % i == 0 or n%(i+2) == 0:
            return False
        i += 6

    return True

if __name__ == "__main__":
    main()