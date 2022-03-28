# Difficulty: Medium

import itertools


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Maintain mapping from digits to possible letters
        For each digit, append list to items
        Create all possible cross-products from items
        """
        if len(digits) == 0:
            return []
        items = []
        letters = {
            "2": list("abc"),
            "3": list("def"),
            "4": list("ghi"),
            "5": list("jkl"),
            "6": list("mno"),
            "7": list("pqrs"),
            "8": list("tuv"),
            "9": list("wxyz"),
        }
        for digit in digits:
            items.append(letters[digit])
        res = ["".join(item) for item in list(itertools.product(*items))]
        return res
