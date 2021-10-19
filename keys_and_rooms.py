# given list of lists of integers
# input rooms = [[1], [2], [3], []]
# index of rooms is the room, the room has list of keys inside the room
# room[i][j] = v where v is the key to room[v]
def solution(rooms):
    seen_hash = {}
    for i in range(len(rooms) - 1):
        seen_hash[i] = False
    seen_hash[0] = True
    print(seen_hash)

    keys = []
    keys.append(0)

    while keys != []:
        key = keys.pop()
        for new_key in rooms[key]:
            if seen_hash[new_key] is False:
                seen_hash[new_key] = True
                keys.append(new_key)


    for room in seen_hash:
        if seen_hash[room] == False:
            return False
    
    return True


