'''
    Merge Two Sorted Lists:
    
    You are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists into a one sorted list.
    The list should be made by splicing together the nodes of the first two lists.
    Return the head of the merged linked list.
'''

class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
def create_list(arr: list[int]) -> ListNode:
    head = ListNode()
    temp1 = head
    for i in range(len(arr)):
        temp2 = ListNode()
        temp1.val = arr[i]
        if i + 1 != len(arr):
            temp1.next = temp2
            temp1 = temp1.next
    return head

def print_list(head: ListNode):
    temp = head
    while temp != None:
        print(temp.val)
        temp = temp.next

def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    if list1 == None:
        return list2
    if list2 == None:
        return list1
    
    new_head = ListNode()
    if list1.val < list2.val:
        new_head = list1
        list1 = list1.next
    else:
        new_head = list2
        list2 = list2.next
        
    temp = new_head
    while list1 != None and list2 != None:
        if list1.val < list2.val:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        temp = temp.next
    
    if list1 == None:
        temp.next = list2
    else:
        temp.next = list1
    
    return new_head

# Testing example
nums1 = [1,2,4]
nums2 = [1,3,4]
list1 = create_list(nums1)
list2 = create_list(nums2)

new_head = merge_two_lists(list1, list2)
print_list(new_head)