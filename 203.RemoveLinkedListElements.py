# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev = ListNode(None)  #宣告偽節點當開頭 並且為前一個節點
        prev.next = current = head  #偽節點的next 為 頭 並作為當前節點開始遍歷
        while current:
            if current.val == val: 
                prev.next = current.next  #當前節點為目標 則上一個節點的next直接跳為當前節點的next
                if current == head: head = head.next    # 刪除頭結點特殊處理
            else:
                prev = current  #沒找到的話前繼續向下找  但有找到的雖然也要向下找 但當前是不要的節點 所以前一個節點固定就好
            current = current.next  #就算找到了一次還是要繼續往下找有無重複的目標
        return head  #輸出完整的head