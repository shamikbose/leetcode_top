# Difficulty: Medium
class Solution:
    """
    DFS based solution. Add '(' until empty, add ')' back in order
    """

    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []
        left, right, ans = n, n, []
        self.dfs(left, right, ans, "")
        return ans

    def dfs(self, left, right, ans, string):
        if right < left:
            return
        if not left and not right:
            ans.append(string)
            return
        if left:
            self.dfs(left - 1, right, ans, string + "(")
        if right:
            self.dfs(left, right - 1, ans, string + ")")

