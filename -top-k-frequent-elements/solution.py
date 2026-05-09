# Submission timestamp: 2026-05-09T05:40:26.327Z

1234581617910121567131411class Solution:    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        ans = []        d = {}        for i in nums:            if i in d:                d[i] += 1                if d[i] == 2:                ans.append(i)            if len(ans) >= 2:                return ans            else:                d[i] = 1
class Solution:    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        ans = []        d = {}        for i in nums:            if i in d:                d[i] += 1                if d[i] == 2:                ans.append(i)            if len(ans) >= 2:                return ans            else:                d[i] = 1
class Solution:
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
ans = []
d = {}
for i in nums:
if i in d:
d[i] += 1
if d[i] == 2:
ans.append(i)
if len(ans) >= 2:
return ans
else:
d[i] = 1
