class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Strip all whitespaces from the left
        Set flag for negative based on first non-whitespace character
        Set num to 0
        As long as current character is numeric, add to 10*num and save to num

        args:
        s: string representing the number

        return:
        num: integer representation of the number
        """
        neg = False
        num = 0
        limit = 2 ** 31 - 1
        s = s.lstrip()
        if not s:
            return 0
        i = 0
        if s[i] == "-":
            neg = True
            i += 1
        elif s[i] == "+":
            i += 1
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        if neg:
            if num > (limit + 1):
                num = -(limit + 1)
            else:
                num = -num
        else:
            if num > limit:
                num = limit
        return num

