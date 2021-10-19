
def solution(root, L, R):
    range_sum = 0
    stack = []
    stack.append(root)

    while stack != []:
        node = stack.pop()
        if node != None:
            if node.val >= L and node.val <= R:
                range_sum += node.val

            if node.val > L:
                stack.append(node.left)

            if node.val < R:
                stack.append(node.right)

    return range_sum


def solution_dfs(root, L, R):

    def recur_dfs(root, L, R, range_sum=0):
        if root != None:
            if root.val >= L and root.val <= R:
                range_sum += root.val

            if root.val >= L:
                recur_dfs(root.left, L, R, range_sum)

            if root.val < R:
                recur_dfs(root.right, L, R, range_sum)

    recur_dfs(root, L, R)