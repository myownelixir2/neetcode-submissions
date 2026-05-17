class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = len(nums) > len(set(nums))
        return dupes
        