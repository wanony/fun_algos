class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(head):
    temp_node = ListNode(0)
    temp_node.next = head
    current = temp_node

    while current.next != None and current.next.next != None:
        first_node = current.next
        second_node = current.next.next
        first_node.next = second_node.next
        current.next = second_node
        current.next.next = first_node
        current = current.next.next

    return temp_node.next