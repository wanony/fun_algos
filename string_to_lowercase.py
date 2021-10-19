
def solution(string):
    result = ""

    for char in string:
        if char.isupper():
            result += chr(ord(char) + 32)
        else:
            result += char

    return result