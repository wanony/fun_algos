
# class ListNode:

#     def __init__(self, val, next_val=None) -> None:
#         self.val = val
#         self.next = ListNode(next_val)


def solution(head):
    previous = None
    while head != None:
        next_node = head.next  # intiate variable with next node
        head.next = previous  # set the next value to the previous one
        previous = head  # make the previous value next value
        head = next_node  # change head node to the next node and repeat

    return previous