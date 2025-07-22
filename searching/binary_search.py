def main():
    print("Binary Search")

    nums1 = [11, 22, 33, 44, 55]

    print(f"11 is present in {nums1}: {binary_search(nums1, 11)}")

    print(f"109 is present in {nums1}: {binary_search(nums1, 100)}")

    nums2 = [11, 22, 33, 44]

    print(f"11 is present in {nums1}: {binary_search(nums2, 11)}")

    print(f"109 is present in {nums1}: {binary_search(nums2, 100)}")


"""
Algorithm
The list should be sorted in ascending order

Step 1: set low = 0 and high = len(list) - 1
Step 2: while low <= high do step 3 to 6
Step 3: calculate median -> (low + high) / 2 
Step 4: check if median value == target, if true return, else step 5
Step 5: check if median is < target, then low = median + 1, else setp 6
Setp 6: check if medain > target then high = median -1
Step 7: if not found return False
"""
def binary_search(nums, target):
    low, high = 0, len(nums) - 1

    while low<=high:
        middle_index = (low + high) // 2
        if nums[middle_index] == target:
            return True
        elif nums[middle_index] < target:
            low = middle_index + 1
        elif nums[middle_index] > target:
            high = middle_index - 1
    
    return False

if __name__ ==  '__main__':
    main()