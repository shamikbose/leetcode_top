# Difficulty: Easy
class Solution:
    def romanToInt(self, s: str) -> int:
        """
        
        """
        symbol_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res, previous = 0, 0
        for c in reversed(s):
            cur_symbol_val = symbol_map[c]
            if cur_symbol_val >= previous:
                res += cur_symbol_val
            else:
                res -= cur_symbol_val
            previous = cur_symbol_val
        return res

