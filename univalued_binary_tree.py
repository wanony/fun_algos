
def solution(root):
    left_unival = root.left == None or root.left.val == root.val and solution(root.left)
    right_unival = root.right == None or root.right.val == root.val and solution(root.right)
    return left_unival and right_unival