# Difficulty: Easy
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Check one element after another for the shortest string. Moment they are mismatched, break

        args:
        strs: list of strings

        return:
        shortest: shortest common prefix in strs
        """
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i in range(len(shortest)):
            for other in strs:
                if other[i] != shortest[i]:
                    return shortest[:i]
        return shortest

