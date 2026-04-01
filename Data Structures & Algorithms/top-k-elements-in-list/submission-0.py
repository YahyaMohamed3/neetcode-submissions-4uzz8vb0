class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_counter = Counter(nums)
        most_common = frequency_counter.most_common(k)
        values = [item[0] for item in most_common]
        return values 

        