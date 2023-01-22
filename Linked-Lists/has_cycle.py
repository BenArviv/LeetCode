'''
    Linked List Cycle:
    
    Given head, the head of a linked list, determine if the linked list has a cycle in it.
    
    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
        following the next pointer.
    Return True if there is a cycle in the linked list.
    Otherwise return False.
'''
class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
def hasCycle(self, head: ListNode) -> bool:
    node_array = []
    temp = head
    
    while temp:
        if temp in node_array:
            return True
        else:
            node_array.append(temp)
            temp = temp.next
    
    return False
