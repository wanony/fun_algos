# ignoring cases!
def solution(string):
    s = ""
    for char in string:
        if char.isdigit() or char.isletter():
            s += char
        
    s = s.lower()

    start = 0
    end = len(s) - 1
    
    while start <= end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1

    return True