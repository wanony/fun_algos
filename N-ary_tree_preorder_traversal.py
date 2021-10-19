# traverses left subtree then right

def solution(root_node):
    stack = []
    output_array = []

    if root_node == None:
        return output_array

    stack.append(root_node)
    while stack != []:
        node = stack[-1]
        output_array.append(node.val)
        node.children.sort(reversed=True)
        for child in node.children:
            stack.append(child)

    return output_array