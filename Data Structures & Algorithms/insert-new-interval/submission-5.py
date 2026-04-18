class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
            res = []
            for i in range(len(intervals)):
                # check if interval comes before
                if newInterval[1] < intervals[i][0]:
                    res.append(newInterval)
                    return res + intervals[i:]
                # check if interval comes after
                elif newInterval[0] > intervals[i][1]:
                    res.append(intervals[i])
                else:
                    # overlapping get min from start and get max from end
                    newInterval = [min(newInterval[0] , intervals[i][0]) , max(newInterval[1] , intervals[i][1])]
            res.append(newInterval)
            return res 
