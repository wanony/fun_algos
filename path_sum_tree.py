
# given a binary tree, determine if the tree has a root to leaf
# path that when adding the node values it equals a given int

def solution(root_node, sum):
    if root_node == None:
        return False

    node_stack = []
    sum_stack = []

    node_stack.append(root_node)
    sum_stack.append(sum - root_node.val)

    while node_stack != []:
        current = node_stack.pop()
        current_sum = sum_stack.pop()

        # this means we have hit a leaf
        if current.left == None and current.right == None:
            if current_sum == 0:
                return True

        if current.left != None:
            node_stack.append(current.left)
            sum_stack.append(current_sum - current.left.val)

        if current.right != None:
            node_stack.append(current.right)
            sum_stack.append(current_sum - current.right.val)

    return False
    