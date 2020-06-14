class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 因為此題只有0, 1, 2 三種值 所以找到0往左邊放,1在中間,2就往右邊放
        left = 0 
        right = len(nums) - 1
        current = 0  #用來遍歷的當前指針
        
        while current <= right:  #從頭找到右邊
            
            if current != left and nums[current] == 0:
                nums[left], nums[current] = nums[current], nums[left]  #找到0時與最左邊的位置交換值
                left += 1  #左邊的往後靠再去交換
                
            elif nums[current] == 2:
                nums[right], nums[current] = nums[current], nums[right]  #找到2時與最右邊的值交換
                right -= 1  #右邊的往前靠再去交換
                
            else:  #指針跟左邊同位置或值為1時繼續往下找
                current += 1