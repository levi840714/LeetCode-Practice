class Solution:
    # 把非0的值丟到最前面排下去 最後再把剩下的補上0
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0  #指向開頭
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[idx] = nums[i]  #找到非0值時丟到前面
                idx += 1  #往下一個index繼續
            
        for i in range(idx, len(nums)):  #最後的index到nums尾端的都補回0
            nums[i] = 0



class Solution:
    # 使用兩個快慢指針去交換位置
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 先找到第一個0當作慢指針 0的下一個位置為快指針
        slow = fast = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                slow, fast = i, i + 1
                break
        
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]  #快指針往下找到不為0的值與慢指針位置交換
                slow += 1  #慢指針往下繼續
            fast += 1
            
        return nums
                    