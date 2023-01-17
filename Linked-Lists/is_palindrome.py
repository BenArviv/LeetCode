'''
    Palindrome Linked List:
    
    Given the head of a singly linked list, return True if it is a palindrome or False otherwise.
'''

class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
def isPalindrome(self, head: ListNode) -> bool:
    list_array = []
    temp = head
    while temp != None:
        list_array.append(temp.val)
        temp = temp.next
    
    n = len(list_array)
    i, j = 0, n - 1
    while i < j:
        if not list_array[i] == list_array[j]:
            return False
        i += 1
        j -= 1

    return True