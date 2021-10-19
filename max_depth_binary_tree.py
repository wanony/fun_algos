
# top down
def solution(root_node, depth=1, answer=None):
    if root_node == None:
        return 0

    if root_node.left == None and root_node.right == None:
        answer = max(answer, depth)

    solution(root_node.left, depth + 1, answer)
    solution(root_node.right, depth + 1, answer)

# bottom up
# i prefer this one, makes more sense to look at
def max_depth(root_node):
    if root_node == None:
        return 0

    left_depth = max_depth(root_node.left)
    right_depth = max_depth(root_node.right)
    return max(left_depth, right_depth) + 1