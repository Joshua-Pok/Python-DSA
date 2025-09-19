## QuickSort is a divide and conquer algorithm, and while it has the same time copmplexity as mergesort it uses less memory

## We pick a pivot, arbitrarily at the end
## We need 2 variables i and j to keep track of things. I  starts at index - 1 and j starts at 0
## We compare j with the pivot, if j is more than pivot we simply increment j
## if j is less than pivot we increment i and swap i and j


def quick_sort(nums, low, high):
    if low < high:
        p = partition(nums, low, high)
        quick_sort(nums, low, p - 1)
        quick_sort(nums, p + 1, high)


def partition(nums, low, high):
    pivot = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    nums[i], nums[high] = nums[high], nums[i]
    return i
