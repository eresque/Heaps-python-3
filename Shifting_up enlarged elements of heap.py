########## Shifting_up enlarged elements of heap ##########

n = int(input())
nums = [int(i) for i in input().split()]

for i in range(int(input())):
    ind, val = [int(i) for i in input().split()]
    nums[ind - 1] += val
    ind -= 1
    while True:
        if ind == 0:
            break
        parents = (ind - 1) // 2
        if nums[parents] > nums[ind]:
            break
        nums[parents], nums[ind] = nums[ind], nums[parents]
        ind = parents
    print(ind + 1)

print(*nums)
