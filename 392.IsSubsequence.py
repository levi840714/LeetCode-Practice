class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if not s: return True
        length = len(s)
        i = 0  #s的index s從頭開始走訪
        for str in t:
            if str == s[i]:
                i += 1;     #找到第一個s後往下繼續找
                if i == length:  #全部都找到返回
                    return True
                
        return False