
def solution(heights):
    start = 0
    end = len(heights) - 1
    max_water = 0

    while start < end:
        if heights[start] < heights[end]:
            max_water = max(max_water, heights[start] * (end - start))
            start += 1
        else:
            max_water = max(max_water, heights[end] * (end - start))
            end -= 1

    return max_water
