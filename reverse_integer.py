
from palindrome_number import solution


def solution(x: int):

    reverse = 0

    while x != 0:
        pop = x % 10
        x = x / 10

        reverse = (reverse * 10) + pop

    return reverse
