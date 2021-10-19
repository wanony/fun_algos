
def solution(nums):
    posi_pointer = 0
    end = len(nums) - 1
    square_array = [None] * (end + 1)

    while posi_pointer < end and nums[posi_pointer] < 0:
        posi_pointer += 1

    negative_pointer = posi_pointer - 1

    i = 0
    while negative_pointer >= 0 and posi_pointer < end:
        if nums[negative_pointer] * nums[negative_pointer] < nums[posi_pointer] * nums[posi_pointer]:
            square_array[i] = nums[negative_pointer] * nums[negative_pointer]
            negative_pointer -= 1
        else:
            square_array[i] = nums[posi_pointer] * nums[posi_pointer]
            posi_pointer += 1
        i += 1

    while negative_pointer >= 0:
        square_array[i] = nums[negative_pointer] * nums[negative_pointer]
        negative_pointer -= 1
        i += 1

    while posi_pointer < end:
        square_array[i] = nums[posi_pointer] * nums[posi_pointer]
        posi_pointer += 1
        i += 1

    return square_array
            
