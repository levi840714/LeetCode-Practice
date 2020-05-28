from math import *
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low  = 0
        high = len(nums) -1
        while low <= high:  #loop 低點到高點交岔處
            mid = (low + high) // 2
            if nums[mid] == target:   #中位數就是目標直接返回
                return mid
            elif nums[mid] > target:  #目標在中位數左邊 高點往中位數左邊-1
                high = mid - 1
            else:                     #目標在中位數右邊 低點往中位數右邊+1
                low  = mid + 1
        return low