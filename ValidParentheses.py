# Difficulty: Easy
class Solution:
    def isValid(self, s: str) -> bool:
        """
        Checks if the parentheses is valid by pushing opening parentheses into a stack and 
        popping them when a closer is found. 
        If the opener and the closer don't match, return False
        If the stack is empty when a closer is found, return False
        If the stack has an element when the string is exhausted, return False

        args:
        s: The string of parentheses

        return:
        boolean value
        """
        stack = []
        openers = ["(", "{", "["]
        closers = [")", "}", "]"]
        # An empty string is valid
        if not s:
            return True
        for c in s:
            if c in openers:
                stack.append(c)
            elif c in closers:
                if not stack:
                    return False
                popped = stack.pop()
                if openers.index(popped) == closers.index(c):
                    continue
                else:
                    return False
        if stack:
            return False
        else:
            return True
