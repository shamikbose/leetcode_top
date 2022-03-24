from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        The idea here is that for every element x at index i in the list, 
        we store `target-x` in a dictionary as the key and i as the value.
        If for an index i, target-x already exists in the dictionary, we 
        return i and the value of the dictionary

        args:
        nums: List of numbers
        target: The target value

        return:
        list(size=2) of indices which sum to the target
        """
        indexMap = {}
        for i, val in enumerate(nums):
            if target - val in indexMap.keys():
                return [i, indexMap[target - val]]
            else:
                indexMap[val] = i

