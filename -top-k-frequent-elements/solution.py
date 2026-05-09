# Submission timestamp: 2026-05-09T05:41:25.343Z

1234710171112168914151356class Solution:    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        ans = []        d = {}        for i in nums:            if i in d:                d[i] += 1                if d[i] == 2:            if len(ans) >= 2:                return ans            else:                d[i] = 1                    ans.append(i)        if k >
class Solution:    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        ans = []        d = {}        for i in nums:            if i in d:                d[i] += 1                if d[i] == 2:            if len(ans) >= 2:                return ans            else:                d[i] = 1                    ans.append(i)        if k >
class Solution:
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
ans = []
d = {}
for i in nums:
if i in d:
d[i] += 1
if d[i] == 2:
if len(ans) >= 2:
return ans
else:
d[i] = 1
ans.append(i)
if k >
