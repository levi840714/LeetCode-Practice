# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                if mid == 1 or not isBadVersion(mid - 1):  #如果mid是1然後前面的也不是壞版本 直接回傳mid
                    return mid
                high = mid - 1  #如果前面也是壞版本的話 高往內縮繼續找
            else:
                low  = mid + 1  #如果mid還不是壞版本 就往後面的版本找     
        return None  #都不是壞版本