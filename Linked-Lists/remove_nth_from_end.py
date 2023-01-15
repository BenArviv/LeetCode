'''
    Remove N-th Node From End of List:
    
    Given the head of a linked list, remove the n-th node from the end of the list and return its head
'''

class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    

def remove_nth_node(head: ListNode, n: int) -> ListNode:
    fast, slow = head, head
    for _ in range(n): fast = fast.next
    if not fast: return head.next
    while fast.next: fast, slow = fast.next, slow.next
    slow.next = slow.next.next
    return head

# Testing example
nums = [1,2,3,4,5]
n = 2
head = ListNode()
temp1 = head
for i in range(len(nums)):
    temp2 = ListNode()
    temp1.val = nums[i]
    temp1.next = temp2
    temp1 = temp1.next
    
new_list = remove_nth_node(head, n)
temp = new_list
while temp.next != None:
    print(temp.val)
    temp = temp.next