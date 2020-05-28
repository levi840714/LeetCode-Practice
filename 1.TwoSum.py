class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        resMap = {}
        for i in range(len(nums)):
            if (target - nums[i]) in resMap: 
                return [resMap[target - nums[i]], i]
            else:
                resMap[nums[i]] = i