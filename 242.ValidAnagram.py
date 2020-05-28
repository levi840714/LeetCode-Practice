class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        res = True
        dirS, dirT = self.calculationStr(s), self.calculationStr(t)
        for i in dirS:
            if i not in  dirT:  #有字不再另一個字典內直接中斷
                res = False
                break
            if dirS[i] != dirT[i]: res = False  #字數量不符合
        return res
        
        
    def calculationStr(self, str):  #算出字串內的字各有多少個
        dic = {}
        for i in str:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        return dic