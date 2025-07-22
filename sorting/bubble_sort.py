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
    swapping = True
    end = len(nums)
    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                temp = nums[i - 1]
                nums[i - 1] = nums[i]
                nums[i] = temp
                swapping = True
        end -= 1
    return nums

print(bubble_sort([33, 22, 11, 44, 23]))