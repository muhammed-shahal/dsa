def main():
    print("Linear Search")
    nums1 = [44, 22, 11, 66, 79]

    print(f"11 is present in {nums1}: {linear_search(nums1, 11)}")

    print(f"109 is present in {nums1}: {linear_search(nums1, 100)}")


"""
Algorithm
Step 1: Loop through all elements in the given array
Step 2: If target value is found return true/index 
Step 3: If not found return false
"""
def linear_search(nums, target):
    for num in nums:
        if target == num:
            return True
        
    return False

if __name__ ==  '__main__':
    main()