# Submission timestamp: 2026-05-09T05:40:03.325Z

1234581516179101114671213class Solution:    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        ans = []        d = {}        for i in nums:            if i in d:                d[i] += 1                d[i] == 2:                ans.append(i)            if len(ans) >= 2:                return ans            else:                d[]
class Solution:    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        ans = []        d = {}        for i in nums:            if i in d:                d[i] += 1                d[i] == 2:                ans.append(i)            if len(ans) >= 2:                return ans            else:                d[]
class Solution:
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
ans = []
d = {}
for i in nums:
if i in d:
d[i] += 1
d[i] == 2:
ans.append(i)
if len(ans) >= 2:
return ans
else:
d[]
