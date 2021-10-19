
def solution(root):
    q = []
    q.append(root)
    
    while q != []:
        root = q.pop(0)
        if root.right != None:
            q.append(root.right)
        if root.left != None:
            q.append(root.left)

    return root.val
