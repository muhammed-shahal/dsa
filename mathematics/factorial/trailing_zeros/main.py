def main():
    print("Trailing Zeros in factorial of a Number")
    print("Number of trailing zeros in factorial of 5:", trailing_zeros(5))
    print("Number of trailing zeros in factorial of 20:", trailing_zeros(20))
    print("Number of trailing zeros in factorial of 100:", trailing_zeros(100))

def trailing_zeros(n):
    count = 0
    i = 5
    
    while i <= n:
        count += n // i
        i *= 5
    
    return count

if __name__ == "__main__":
    main()