def main():
    print("Factorial")
    print("factorial of 5", factorial(5))
    print("factorial of 6", factorial_recursive(6))


def factorial(n):
    
    if n <= 1:
        return n
    
    fact = 1

    for i in range(2, n+1):
        fact *= i
    
    return fact

def factorial_recursive(n):
    if n == 1:
        return 1
    
    return n * factorial_recursive(n-1)

if __name__ == "__main__":
    main()