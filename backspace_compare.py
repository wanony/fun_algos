# given two strings S and T, return if they are equal
# if the strings contain a # symbol, it is a backspace
# therefore deleting the previous character

def solution(s, t):
    s_pointer = len(s) - 1
    t_pointer = len(t) - 1

    s_skip = 0
    t_skip = 0

    while s_pointer >= 0 or t_pointer >= 0:

        while s_pointer >= 0:
            if s[s_pointer] == '#':
                s_skip += 1
                s_pointer -= 1
            elif s_skip > 0:
                s_pointer -= 1
                s_skip -= 1
            else:
                break

        while t_pointer >= 0:
            if t[t_pointer] == '#':
                t_skip += 1
                t_pointer -= 1
            elif t_skip > 0:
                t_pointer -= 1
                t_skip -= 1
            else:
                break
        
        if s_pointer >= 0 and t_pointer >=0 and s[s_pointer] != t[t_pointer]:
            return False

        if s_pointer >= 0 != t_pointer >= 0:
            return False
        
        s_pointer -= 1
        t_pointer -= 1
        
    return True