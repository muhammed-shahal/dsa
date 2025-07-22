import math

def main():
    print("Count Digits")

    print(f"Number of digits in 12345 is: {count_digits(12345)}")

    print(f"Number of digits in 9876543210 is {count_digits_using_log(987654321)}")

def count_digits(num):
    count = 0

    while num > 0:
        num = num//10
        count +=1
    
    return count

def count_digits_using_log(num):
    return math.floor(math.log(num, 10) + 1)


if __name__ == "__main__":
    main()