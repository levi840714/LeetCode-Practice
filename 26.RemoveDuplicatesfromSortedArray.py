class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if not nums: return 0
        
        i, j = 0, 1   # i用來比對 j用來往下遍歷
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1   #找到不同的時候 i + 1 計數有不同的值
                nums[i] = nums[j] #把i位置的值替換掉成j的值  這樣下一個j還是一樣值的時候才不會重複又紀錄 (!!因為此題不在乎原本陣列值 所以才直接修改)
            j += 1  #往下繼續遍歷
            
        return i + 1  #因為i是從0開始計數 所以長度要+1