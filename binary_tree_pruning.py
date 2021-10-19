
def solution(root):
    if root is None:
        return None
    
    def contains_a_one(node):
        if node == None:
            return False
        left_has = contains_a_one(node.left)
        right_has = contains_a_one(node.right)
        if not left_has:
            node.left = None
        if not right_has:
            node.right = None

        return node.val == 1 or left_has or right_has

    if not contains_a_one(root):
        root = None

    return root