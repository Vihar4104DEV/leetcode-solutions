# Submission timestamp: 2026-05-09T05:54:55.338Z

123456class Solution:    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        freq = {}        for num in nums:            freq[num] = freq.get(num)
class Solution:    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        freq = {}        for num in nums:            freq[num] = freq.get(num)
class Solution:
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
freq = {}
for num in nums:
freq[num] = freq.get(num)
