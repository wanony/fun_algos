# given an array of integers, find if there are any duplicates in the array

# example

# input: [1, 2, 3, 1]

# output: True


# hash set solution, O(N) space and time

def hash_solution(nums):
    hash = {}
    for n in nums:
        if n in hash:
            return True
        
        hash[n] = 0

    return False


# sorting method, O(N), no extra space required

def sort_solution(nums):
    nums.sort()

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True

    return False



numbers = [1, 35, 22, 3, 3, 96, 7, 0]
numbers_2 = [1, 35, 22, 3, 96, 7, 0]

print(hash_solution(numbers))
print(sort_solution(numbers))
print(hash_solution(numbers_2))
print(sort_solution(numbers_2))