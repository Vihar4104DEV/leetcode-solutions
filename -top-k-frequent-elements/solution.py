# Submission timestamp: 2026-05-09T05:42:10.336Z

123481112131791015161457618class Solution:    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        ans = []        d = {}        for i in nums:            if i in d:                d[i] += 1                if d[i] == 2:            if len(ans) >= 2:                return ans            else:                d[i] = 1                    ans.append(i)        if k <=1:            return [nums[0]]
class Solution:    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        ans = []        d = {}        for i in nums:            if i in d:                d[i] += 1                if d[i] == 2:            if len(ans) >= 2:                return ans            else:                d[i] = 1                    ans.append(i)        if k <=1:            return [nums[0]]
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
if k <=1:
return [nums[0]]
