########### Shifting_down decreased elements of the heap ###########

n = int(input())
nums = [int(i) for i in input().split()]

for i in range(int(input())):
    ind, val = [int(i) for i in input().split()]
    ind -= 1
    nums[ind] -= val
    while True:
        if ind * 2 + 1 >= n:
            break
        if ind * 2 + 2 < n:
            if nums[ind * 2 + 1] > nums[ind * 2 + 2]:
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
    print(ind + 1)

print(*nums)
