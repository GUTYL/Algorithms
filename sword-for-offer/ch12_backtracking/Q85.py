from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.helper(n, n, "", result)
        return result

    def helper(self, left, right, parenthesis, result):
        if left == 0 and right == 0:
            return result.append(parenthesis)
        if left > 0:
            self.helper(left - 1, right, parenthesis + '(', result)
        if right > left:
            self.helper(left, right - 1, parenthesis + ')', result)
