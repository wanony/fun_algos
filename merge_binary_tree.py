
# class TreeNode:
#     def __init__(self, val, left, right) -> None:
#         self.val = val
#         self.left = left
#         self.right = right


def solution(tree_1, tree_2):
    if tree_1 == None:
        return tree_2

    if tree_2 == None:
        return tree_1

    tree_1.val += tree_2.val

    tree_1.left = solution(tree_1.left, tree_2.left)
    tree_1.right = solution(tree_1.right, tree_2.right)

    return tree_1