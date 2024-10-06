# Notes: 
# 

# Time  Complexity: O(n)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ### Approach 1 - recrusive
        # if not currHead:
        #     return None

        # newHead = currHead
        # if currHead.next:
        #     newHead = self.reverseList(currHead.next)
        #     currHead.next.next = head
        # head.next = None

        # return newHead

        ### Approach 2 - iterative
        prev = None
        curr = head

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev



