
# check if a binary tree is symmetric

def solution(root_node):

    def is_mirror(tree_1, tree_2):
        if tree_1 == None and tree_2 == None:
            return True
        if tree_1 == None or tree_2 == None:
            return False
        
        return (tree_1.val == tree_2.val) and is_mirror(tree_1.left, tree_2.right) and is_mirror(tree_1.right, tree_2.left)

    return is_mirror(root_node, root_node)