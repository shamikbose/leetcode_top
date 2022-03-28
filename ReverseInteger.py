class Solution:
    def reverse(self, x: int) -> int:
        """
        If number is negative, make it positive
        Read digits into a list in reverse order
        Convert that back into an integer
        Restore original sign

        args:
        x: int

        return:
        res: int
        """
        digits = []
        temp_x = x
        if x == 0:
            return 0
        elif x < 0:
            x *= -1
        while x > 0:
            digits.append(str(x % 10))
            x = x // 10
        if digits[0] == "0":
            digits = digits[1:]
        res = int(("").join(digits))
        if temp_x < 0:
            res *= -1
        if res > 2 ** 31 - 1 or res < -(2 ** 31):
            return 0
        return res
