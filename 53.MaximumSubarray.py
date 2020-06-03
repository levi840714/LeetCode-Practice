class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums
        for i in range(1, len(nums)):
            #比較最大值是從當前這個開始 還是 當前之前相加的最大值
            dp[i] = max(dp[i], dp[i] + dp[i - 1])
            
        return max(dp)