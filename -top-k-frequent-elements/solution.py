# Submission timestamp: 2026-05-09T05:48:30.329Z

811121391015161476175181920421        for i in nums:            if i in d:                d[i] += 1                if d[i] == k:            if len(ans) >= k:                return ans            else:                d[i] = 1                    ans.append(i)            return [nums[0]]        print(d)        if k <=1 and len(nums) == 1:        return [max(d, key=d.get)]        return ans        d = {}
for i in nums:            if i in d:                d[i] += 1                if d[i] == k:            if len(ans) >= k:                return ans            else:                d[i] = 1                    ans.append(i)            return [nums[0]]        print(d)        if k <=1 and len(nums) == 1:        return [max(d, key=d.get)]        return ans        d = {}
for i in nums:
if i in d:
d[i] += 1
if d[i] == k:
if len(ans) >= k:
return ans
else:
d[i] = 1
ans.append(i)
return [nums[0]]
print(d)
if k <=1 and len(nums) == 1:
return [max(d, key=d.get)]
return ans
d = {}
