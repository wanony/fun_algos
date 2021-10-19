
def solution(root_node):
    if root_node == None:
        return root_node

    left = solution(root_node.left)
    right = solution(root_node.right)

    root_node.right = left
    root_node.left = right

    return root_node