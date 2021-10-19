
# given a version number, find first bad version
# all following versions from first bad are bad

def isBadVersion(n):
    if n >= 25:  # this would be different for each solution
        return True
    else:
        return False

def solution(n):

    left = 0
    right = n

    while left < right:
        mid = left + (right - left) / 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
        
    if left == right and isBadVersion(left):
        return left

    return -1