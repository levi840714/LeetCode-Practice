# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: return True  #兩個節點都為空則相等
        if not p or not q: return False  #一個節點有值另一個為空則不相等
        #都有值 值也相等 左右兩邊遞迴下去比對也相等則兩棵樹為一樣
        if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right): return True