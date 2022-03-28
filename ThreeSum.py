# Difficulty: Medium
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Sort the array nums
        if the first element of the sorted array is greater than zero, return emoty list since sum cannot be zero
        For every element till the second last one
            Maintain two pointers, one to the immediate right(l) and another to the end(r)
            Add all three
            If sum > 0, move r left
            If sum < 0, move l right
            If sum = 0, append tuple to result
        """
        res = []
        nums.sort()
        if len(nums) > 0 and nums[0] > 0:
            return res
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res

