# in order traverses left subtree, then root node
# then the right subtree

# input [1, None, 2, 3]
# output [1, 3, 2]


def solution(root_node):

    stack = []
    output_array = []

    if root_node == None:
        return output_array

    current = root_node

    while current != None or stack != []:
        while current != None:
            stack.append(current)
            current = current.left

        current = stack.pop()
        output_array.append(current.val)
        current = current.right

    return output_array