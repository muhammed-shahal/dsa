def selection_sort(nums):
    for i in range(0, len(nums)):
        index = i
        
        for j in range(i+1, len(nums)):
            if nums[j] < nums[index]:
                index = j
        
        temp = nums[i]
        nums[i] = nums[index]
        nums[index] = temp

    
    print(nums)

nums = [7, 2, 5, 4, 1, 6, 0, 3]

selection_sort(nums)
