
def solution(x: int):
    if x == 0:
        return True

    if x < 0 or x % 10 == 0:
        return False

    reverse_int = 0

    while x > reverse_int:
        pop = x % 10

        x = x / 10

        reverse_int = (reverse_int * 10) + pop

    if x == reverse_int or x == reverse_int / 10:
        return True
    else:
        return False