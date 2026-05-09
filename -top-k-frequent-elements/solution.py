# Submission timestamp: 2026-05-09T05:56:21.328Z

1234567891011class Solution:    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        freq = {}        for num in nums:            freq[num] = freq.get(num,0) + 1        s_nums = sorted(freq, key=freq.get, reverse=True)        return s_nums[:k]
class Solution:    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        freq = {}        for num in nums:            freq[num] = freq.get(num,0) + 1        s_nums = sorted(freq, key=freq.get, reverse=True)        return s_nums[:k]
class Solution:
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
freq = {}
for num in nums:
freq[num] = freq.get(num,0) + 1
s_nums = sorted(freq, key=freq.get, reverse=True)
return s_nums[:k]
