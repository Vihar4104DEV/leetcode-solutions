# Submission timestamp: 2026-05-09T05:44:06.328Z

348111213910151614576171819        ans = []        d = {}        for i in nums:            if i in d:                d[i] += 1                if d[i] == 2:            if len(ans) >= 2:                return ans            else:                d[i] = 1                    ans.append(i)        if k <=1:            return [nums[0]]                for i in d.items
ans = []        d = {}        for i in nums:            if i in d:                d[i] += 1                if d[i] == 2:            if len(ans) >= 2:                return ans            else:                d[i] = 1                    ans.append(i)        if k <=1:            return [nums[0]]                for i in d.items
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
for i in d.items
