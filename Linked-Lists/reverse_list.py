'''
    Reverse Linked List:
    
    Given the head of a singly linked list, reverse the list, and return the reversed list
'''

class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
def reverseList(head: ListNode) -> ListNode:
    temp1 = head
    temp2 = temp1.next
    if temp2 == None: # List contain only one node
        return head
    
    temp3 = temp1.next
    temp1.next = None
    while temp3.val != 0:
        temp3 = temp3.next
        temp2.next = temp1
        temp1 = temp2
        temp2 = temp3
    new_head = temp1
    return new_head

# Testing example
nums = [1,2]
n = 2
head = ListNode()
temp1 = head
for i in range(len(nums)):
    temp2 = ListNode()
    temp1.val = nums[i]
    temp1.next = temp2
    temp1 = temp1.next
    
new_list = reverseList(head)
temp = new_list
array = []
while temp != None:
    array.append(temp.val)
    temp = temp.next
print(array)