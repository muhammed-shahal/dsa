"""
Algorithm

1. Set Swapping = True
2. Set end = length of list
3. While Swapping True
    a. set swapping = false
    b. for i from 2nd element to end
        if i-1 elem > i elem
        swap i-1 and i
        set swapping = True
    c. Decrement end by 1
4. Return Sorted list
"""

def bubble_sort(nums):
    for i in range(0, len(nums) - 1):
        swap = False
        for j in range(0, len(nums) - 2):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] =  nums[j+1]
                nums[j+1] = temp
                swap = True
        
        if not swap:
            break
    
    print(nums)

print(bubble_sort([33, 22, 11, 44, 23]))