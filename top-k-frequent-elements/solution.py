# Submission timestamp: 2026-05-09T05:44:22.339Z

4811121391015161457617181920        d = {}        for i in nums:            if i in d:                d[i] += 1                if d[i] == 2:            if len(ans) >= 2:                return ans            else:                d[i] = 1                    ans.append(i)        if k <=1:            return [nums[0]]                for i in d.keys():            ans.append(i)
d = {}        for i in nums:            if i in d:                d[i] += 1                if d[i] == 2:            if len(ans) >= 2:                return ans            else:                d[i] = 1                    ans.append(i)        if k <=1:            return [nums[0]]                for i in d.keys():            ans.append(i)
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
for i in d.keys():
ans.append(i)
