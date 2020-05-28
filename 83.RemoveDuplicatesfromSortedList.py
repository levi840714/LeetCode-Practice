# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        preNode = head  #先assign一個變數 用來遍歷找節點
        while preNode:  #遍歷直到None
            nextNode = preNode.next  #當前節點的下一個節點用來遍歷
            while nextNode and nextNode.val == preNode.val:  #下一個節點有值並與當前節點值相同
                nextNode = nextNode.next  #繼續往下找
            preNode.next = nextNode  #跳出條件把當前節點指到不重複的節點
            preNode = preNode.next  #繼續往下一輪
        return head