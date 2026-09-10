# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []

        cur = head
        while cur:
            temp.append(cur.val)
            cur = cur.next
        
        temp.reverse()

        cur = head
        for i in range(len(temp)):
            cur.val = temp[i]
            cur = cur.next
        
        return head