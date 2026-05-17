class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        for i, n in enumerate(nums):
            for j in nums[:i] + nums[i+1 :]:
                if (n+j) == target:
                    indices.append(i)
        return indices
