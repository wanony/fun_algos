
def solution(head):
    if head == None:
        return None
    
    odd = head
    even = head.next
    even_head = even

    while even != None and even.next != None:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_head

    return head