# Submission timestamp: 2026-05-09T05:25:47.019Z

1234567class Solution:    def majorityElement(self, nums: List[int]) -> int:        count = 0        candidate = None        for num in nums:            if count == 0:
