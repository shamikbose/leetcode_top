# Difficulty: Medium
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Iterate through position of every character
        Find longest substring from that position in either direction
        Return longest of all such substrings
        args:
        s: Input string
        
        return:
        Longest palindromic substring
        """
        res = ""
        for i in range(len(s)):
            tmp_odd = self.helper(s, i, i)
            tmp_even = self.helper(s, i, i + 1)
            lrgr = tmp_even if len(tmp_even) > len(tmp_odd) else tmp_odd
            if len(lrgr) > len(res):
                res = lrgr
        return res

    def helper(self, s: str, l: int, r: int):
        """
        Return longest palindromic substring from any position
        args:
        s: input string
        l: position of left pointer
        r: position of right pointer

        return:
        Longest palindromic substring 
        """
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # Move left pointer to the left, right pointer to the right
            l -= 1
            r += 1
        return s[l + 1 : r]

