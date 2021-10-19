class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(head, x):
    before_head = ListNode(0)
    before = before_head
    after_head = ListNode(0)
    after = after_head

    while head != None:
        if head.val < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next

        head = head.next

    after.next = None
    before.next = after_head.next

    return before_head.next