class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # case 1 new interval come before
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # case 2 new interval comes after
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            else:
                #they over lap
                newInterval = [min(newInterval[0] , intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res 
