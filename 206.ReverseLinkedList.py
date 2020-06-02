# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, current = None, head
        while current:
            nxt = current.next  #先把下一個節點暫存起來
            current.next = prev #下一節個點直接指向上一節點反轉
            prev    = current
            current = nxt
            
        return prev