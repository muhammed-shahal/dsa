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

# Leetcode Problem
# Count the Digits That Divide a Number
# https://leetcode.com/problems/count-the-digits-that-divide-a-number
def count_digits_that_divides_number(num):
    """
    :type num: int
    :rtype: int
    """

    count = 0
    temp = num
    while temp > 0:
        if num % (temp % 10) == 0:
            count +=1
        temp = temp//10
    
    return count

if __name__ == "__main__":
    main()