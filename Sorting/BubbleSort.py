def BubbleSort(nums):
    swapped = True
    end = len(nums)
    while swapped == True:
        swapped = False
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                temp = nums[i]
                nums[i] = nums[i - 1]
                nums[i - 1] = temp
                swapped = True
        end -= 1
        


