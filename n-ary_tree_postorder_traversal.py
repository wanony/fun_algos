
# Definition for a node

# class Node:
#     def __init__(self, val: int, children: list) -> None:
#         self.val = val
#         self.children = children

# 'postorder' means that the root will be traversed last

def solution(root_node):
    stack = []
    output_array = []
    if root_node == None:
        return output_array

    stack.append(root_node)

    while stack != []:
        node = stack[-1]
        output_array.insert(0, node)
        for child in node.children:
            stack.append(child)

    return output_array