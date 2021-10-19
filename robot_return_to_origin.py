# string array of moves, Up Down Left Right, check if
# robot returns to coordinate (0,0)
def solution(moves):
    x = 0
    y = 0

    for char in moves:
        if char == 'U':
            y += 1
        elif char == 'D':
            y -= 1
        elif char == 'L':
            x -= 1
        elif char == 'R':
            x += 1

    return x == 0 and y == 0