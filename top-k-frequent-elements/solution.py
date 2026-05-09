# Submission timestamp: 2026-05-09T05:51:47.329Z

151614171819202122232413121110987            else:                d[i] = 1                    ans.append(i)            max_value = max(d.values())        max_keys = [k for k, v in d.items() if v == max_value]        return max_keys                if d[i] == k:                d[i] += 1            if i in d:                return ans            if len(ans) >= k:        for i in nums:
else:                d[i] = 1                    ans.append(i)            max_value = max(d.values())        max_keys = [k for k, v in d.items() if v == max_value]        return max_keys                if d[i] == k:                d[i] += 1            if i in d:                return ans            if len(ans) >= k:        for i in nums:
else:
d[i] = 1
ans.append(i)
max_value = max(d.values())
max_keys = [k for k, v in d.items() if v == max_value]
return max_keys
if d[i] == k:
d[i] += 1
if i in d:
return ans
if len(ans) >= k:
for i in nums:
