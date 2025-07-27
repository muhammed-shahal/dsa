def main():
    print("GCD or HCF")

    print(f"GCD of 4, 6 is: {gcd_euclidean(4, 6)}")
    print(f"GCD of 15, 20 is: {gcd_euclidean(15, 20)}")


"""
Algorithm
Step 1: FInd the minimum. bcz values bigger than min won't be common divisor
Step 2: Loop backwards from min to zero and check whether it divides both numbers
Step 3. If it's return the number
Step 4: ELse return no hcf
"""
def gcd_or_hcf_naive(x, y):
    min_value =  min(x, y)
    for i in range(min_value, 0, -1):
        if (x% i == 0) and (y % i == 0):
            return i
    
    return -1

def gcd(x, y):
    while x > 0 and y > 0:
        if x > y:
            x = x %y
        else:
            y = y % x
    
    if x == 0:
        return y
    
    return x

def gcd_euclidean(x, y):
    while x != y:
        if x >= y:
            x = x-y
        else:
            y=y-x
    
    return x

# Leetcode Problem
# https://leetcode.com/problems/find-greatest-common-divisor-of-array/
def find_gcd_in_array(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    maximum = float("-inf")
    minimum = float("inf")

    for num in nums:
        if num > maximum:
            maximum = num
        
        if num < minimum:
            minimum = num

    while minimum > 0 and maximum > 0:
        if maximum >= minimum:
            maximum = maximum % minimum
        else:
            minimum = minimum % maximum
    
    if maximum == 0:
        return minimum

    return maximum

if __name__ == "__main__":
    main()