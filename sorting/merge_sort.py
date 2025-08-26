def merge_sort(nums):
    if len(nums) == 1:
        return nums
    

    left = merge_sort(nums[:len(nums)//2])
    right = merge_sort(nums[len(nums)//2 :])
    return merge(left, right)

def merge(left, right):
    i, j = 0, 0

    new = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            new.append(left[i])
            i+=1
        else:
            new.append(right[j])
            j+=1
    
    while i < len(left):
        new.append(left[i])
        i+=1

    while j < len(right):
        new.append(right[j])
        j+=1
    
    return new

nums = [7, 2, 5, 4, 1, 6, 0, 3]

print(merge_sort(nums))