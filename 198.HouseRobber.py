class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if not nums: return 0
        if length == 1: return nums[0]
        dp = [0] * length  #建造一個長度等於nums的dp來記錄
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, length):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])  #當前這家+兩家前的最大值總和 或是 前一家的最大值總和  這兩個去比較
            
        return dp[-1]  #返回最後一個dp max(dp)