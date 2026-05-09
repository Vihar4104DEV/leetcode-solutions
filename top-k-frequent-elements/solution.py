# Submission timestamp: 2026-05-09T05:42:20.326Z

34811121391015161457617182        ans = []        d = {}        for i in nums:            if i in d:                d[i] += 1                if d[i] == 2:            if len(ans) >= 2:                return ans            else:                d[i] = 1                    ans.append(i)        if k <=1:            return [nums[0]]                    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
ans = []        d = {}        for i in nums:            if i in d:                d[i] += 1                if d[i] == 2:            if len(ans) >= 2:                return ans            else:                d[i] = 1                    ans.append(i)        if k <=1:            return [nums[0]]                    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
