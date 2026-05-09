# Submission timestamp: 2026-05-09T05:39:29.326Z

123457121314891011615class Solution:    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        ans = []        d = {}        for i in nums:            if i in d:                d[i] += 1                d[i] == 2:                ans.append(i)            if len(ans)
class Solution:    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        ans = []        d = {}        for i in nums:            if i in d:                d[i] += 1                d[i] == 2:                ans.append(i)            if len(ans)
class Solution:
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
ans = []
d = {}
for i in nums:
if i in d:
d[i] += 1
d[i] == 2:
ans.append(i)
if len(ans)
