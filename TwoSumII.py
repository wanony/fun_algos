# given an array of integers that is already sorted in ascending order,
# find two numbers such that they add up to a specific target number

# the function should return the indicies of the two numbers by order
# of first appearance

# example

# input: [2, 7, 11, 15], 9

# output: [0, 1]


def solution(numbers: list, target: int):
    
    # set up two pointers to move up or down
    start = 0
    end = len(numbers) - 1

    while start <= end:
        summ = numbers[start] + numbers[end]

        if summ > target:
            end -= 1
        elif summ < target:
            start += 1
        else:
            return [start, end]

    return [start, end]


print(solution([1, 5, 12, 14, 15, 99, 105], 13))