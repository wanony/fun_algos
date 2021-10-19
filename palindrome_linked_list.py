# definition for node class

# class ListNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
def reversed_list(head):
    prev = None
    while head != None:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    
    return prev

def solution(head):
    slow = head
    fast = head
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
    slow = reversed_list(slow)
    fast = head

    while slow != None:
        if slow.val != fast.val:
            return False
        slow = slow.next
        fast = fast.next
    
    return True

