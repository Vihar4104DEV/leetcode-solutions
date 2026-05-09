# Submission timestamp: 2026-05-09T05:51:45.333Z

1516141718192021222324252613121110            else:                d[i] = 1                    ans.append(i)            max_value = max(d.values())        max_keys = [k for k, v in d.items() if v == max_value]        return max_keys                        if d[i] == k:                d[i] += 1            if i in d:                return ans
else:                d[i] = 1                    ans.append(i)            max_value = max(d.values())        max_keys = [k for k, v in d.items() if v == max_value]        return max_keys                        if d[i] == k:                d[i] += 1            if i in d:                return ans
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
