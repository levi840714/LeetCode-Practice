class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, minBuy = 0, float('inf')
        for i in prices:
            minBuy = min(minBuy, i)  #找出當前最小的買入價格保存
            profit = max(profit, i - minBuy)  #當前價格 - 最小買入 找最大收益
                
        return profit