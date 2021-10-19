
def solution(nums, target):
    # array of ints, find 3 that sum closest to the target
    # return the sum of the numbers
    difference = 0
    result = nums[0] + nums[1] + nums[(len(nums) - 1)]
    nums.sort()

    for i in range(len(nums) - 2):
        start = i + 1
        end = len(nums) - 1
        
        while start < end:
            c_sum = nums[i] + nums[start] + nums[end]
            if c_sum > target:
                end -= 1
            else:
                start += 1

            if abs(c_sum - target) < abs(result - target):
                result = c_sum

    return result
