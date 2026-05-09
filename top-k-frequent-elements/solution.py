# Submission timestamp: 2026-05-09T05:39:02.326Z

123456910117812class Solution:    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        ans = []        d = {}        for i in nums:            if i in d:                d[i] += 1    d[i]
class Solution:    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        ans = []        d = {}        for i in nums:            if i in d:                d[i] += 1    d[i]
class Solution:
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
ans = []
d = {}
for i in nums:
if i in d:
d[i] += 1
d[i]
