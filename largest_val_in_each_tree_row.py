
def solution(root):
    # return list of ints of largest values of each row.
    result = []
    def tree_searcher(root, result, level):
        if root == None:
            return

        if level == len(result):
            result.append(root.val)
        else:
            result[level] = max(result[level], root.val)

        tree_searcher(root.left, result, level + 1)
        tree_searcher(root.right, result, level + 1)

    tree_searcher(root, result, 0)

    return result
