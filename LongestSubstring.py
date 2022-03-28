# Difficulty: Medium
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Takes s as input and returns the longest substring without repeated characters
        Approach: 
        Maintain a dictionary of used charcters. Read characters in string s. 
        Iterate through s. Maintain last position you saw the current character and return 
        the max of previous max length and current non-repeated substring
        args: 
        s: string

        return:
        maxLength: int
        """
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            # If s[i] is already in current substring
            if s[i] in usedChar and start <= usedChar[s[i]]:
                # Update start
                start = usedChar[s[i]] + 1
            else:
                # Update maxLength
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i
        return maxLength
