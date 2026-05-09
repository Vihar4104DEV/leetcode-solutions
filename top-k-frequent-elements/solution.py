# Submission timestamp: 2026-05-09T05:55:52.326Z

12345678910class Solution:    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        freq = {}        for num in nums:            freq[num] = freq.get(num,0) + 1        s_nums = sorted(freq, key=freq.get, reverse)
class Solution:    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        freq = {}        for num in nums:            freq[num] = freq.get(num,0) + 1        s_nums = sorted(freq, key=freq.get, reverse)
class Solution:
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
freq = {}
for num in nums:
freq[num] = freq.get(num,0) + 1
s_nums = sorted(freq, key=freq.get, reverse)
