# given a non-negative interger num_rows, generate the first num_rows
# arrays of Pascal's triangle

# example

# input: 5

# output:
# [
#         [1], 
#        [1,1], 
#       [1,2,1], 
#      [1,3,3,1], 
#     [1,4,6,4,1]
# ]


def solution(num_rows: int):

    triangle = [[1]]
    if num_rows == 0:
        return triangle

    i = 1
    while i < num_rows:
        previous_row = triangle[i - 1]
        row = [1]

        j = 1
        while j < i:
            row.append(previous_row[j - 1] + previous_row[j])
            j += 1

        i += 1
        row.append(1)
        triangle.append(row)

    return triangle


print(solution(3))