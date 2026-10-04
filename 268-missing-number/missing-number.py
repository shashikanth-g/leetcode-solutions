class Solution:
    def missingNumber(self, nums):
        n = len(nums)

        numbers = set(nums)

        for i in range(n + 1):
            if i not in numbers:
                return i