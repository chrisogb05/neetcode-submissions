class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev = None
        for n in sorted(nums):
            if n == prev:
                return True
            prev = n
        return False

            