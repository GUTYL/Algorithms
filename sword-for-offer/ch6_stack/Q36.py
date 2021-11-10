from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tmp = []
        for i in tokens:
            if i in "+-*/":
                b = tmp.pop()
                a = tmp.pop()
                if i == '+':
                    tmp.append(a + b)
                elif i == '-':
                    tmp.append(a - b)
                elif i == '*':
                    tmp.append(a * b)
                else:
                    tmp.append(int(a / b))
            else:
                tmp.append(int(i))
        return tmp.pop()
