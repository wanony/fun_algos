# if there are two middle nodes, return the second one
def solution(head):
    head_pointer = head
    end_pointer = head

    # use standard fast/slow pointer approach
    while end_pointer != None and end_pointer.next != None:
        head_pointer = head_pointer.next
        end_pointer = end_pointer.next.next

    return head_pointer