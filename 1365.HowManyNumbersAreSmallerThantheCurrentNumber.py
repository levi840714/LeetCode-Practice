class ForSolution:  #暴力解 兩個loop去跑過所有累加有大於多少個值
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = []
        for i in nums:
            count = 0
            for j in nums:
                if i > j:
                    count += 1
            arr.append(count)
            
        return arr


class SortSolution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortNums = sorted(nums)
        return [sortNums.index(i) for i in nums]  #排序後的索引位置代表有多少個值比你小        