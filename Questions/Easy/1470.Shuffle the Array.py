def Shuffle(nums,n):
    arr_x = nums[0:n]
    arr_y = nums[n:len(nums)]
    result = []
    for i in range(n):
        result.append(arr_x)
        result.append(arr_y)
    return result