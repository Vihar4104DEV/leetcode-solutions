# Submission timestamp: 2026-05-09T05:50:42.331Z

81112139101516147617518192120        for i in nums:            if i in d:                d[i] += 1                if d[i] == k:            if len(ans) >= k:                return ans            else:                d[i] = 1                    ans.append(i)            return [nums[0]]            if k <=1 and len(nums) == 1:        max_values = max(d.values())        max_keys = [k for k, v in d.items() if v == max_value]        return ans        return max
for i in nums:            if i in d:                d[i] += 1                if d[i] == k:            if len(ans) >= k:                return ans            else:                d[i] = 1                    ans.append(i)            return [nums[0]]            if k <=1 and len(nums) == 1:        max_values = max(d.values())        max_keys = [k for k, v in d.items() if v == max_value]        return ans        return max
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
if k <=1 and len(nums) == 1:
max_values = max(d.values())
max_keys = [k for k, v in d.items() if v == max_value]
return ans
return max
