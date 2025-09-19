def merge_sort(nums):
    if len(nums) < 2:
        return nums #no need to sort if only 1 item

    first = merge_sort(nums[: len(nums) // 2])
    second = merge_sort(nums[len(nums) // 2:])

    #recursively split array until thye become single elements => single elements are always sorted.
    return merge(first, second)



def merge(first, second):
    final = []
    i = 0
    j = 0 
    while i < len(first) and j < len(second):
        if(first[i] <= second[j]):
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1

    while i < len(first):
        final.append(first[i])
        i +=  1

    while j < len(second):
        final.append(second[j])
        j += 1
    
    return final
    
## We have 2 arrays first and second, and we compare and add the smaller one, if only one array has items left we just keep adding.


