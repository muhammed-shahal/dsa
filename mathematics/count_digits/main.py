import math

def main():
    print("Count Number of digits")
    print("no of digits in 12345", count_digits(12345))
    print("no of digits in 12345", count_digits_using_log(12345))
    

def count_digits(n):
    count = 0

    while n > 0:
        n = n // 10
        count += 1
    
    return count

def count_digits_using_log(n):
    return int(math.log(n, 10) + 1)

if __name__ == "__main__":
    main()