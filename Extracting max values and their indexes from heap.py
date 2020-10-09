############ Extracting max values and their indexes from heap ############

n = int(input())
nums = [int(i) for i in input().split()]

for i in range(n):
    ind, val = 0, nums[0]
    nums[0] = nums[n - 1]
    n -= 1
    while True:
        if ind * 2 + 1 >= n:
            break
        if ind * 2 + 2 < n:
            if nums[ind * 2 + 1] >= nums[ind * 2 + 2]:
                child = ind * 2 + 1
            else:
                child = ind * 2 + 2
            if nums[ind] > nums[child]:
                break
            nums[ind], nums[child] = nums[child], nums[ind]
            ind = child
        else:
            child = ind * 2 + 1
            if nums[ind] > nums[child]:
                break
            nums[ind], nums[child] = nums[child], nums[ind]
            ind = child
    if n != 0:
        print(ind + 1, val)
