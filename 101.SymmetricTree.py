# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.recu(root.left, root.right)  #左右子樹丟去遞迴比較
    
    def recu(self, left, right):
        if not left and not right: return True
        if (not left or not right) or left.val != right.val: return False  #左右節點其中一個為空 或 兩邊值不相等 則不是對稱
        #滿足對稱條件: 左子樹的左節點 = 右子樹右節點 and 左子樹右節點 = 右子樹左節點
        return self.recu(left.left, right.right) and self.recu(left.right, right.left)