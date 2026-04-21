class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # check if new interval's end is after the intervals start if end < start then it comes before
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]: # if the start is bigger than the interval end then it comes after
                res.append(intervals[i])
            else:
                # they over lap merge them by taking the min of the both intervals setting it to start and taking max setting it to end 
                newInterval = [min(newInterval[0] , intervals[i][0]), max(newInterval[1] , intervals[i][1])]
        res.append(newInterval)
        return res 

