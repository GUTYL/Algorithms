from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        input_stack = []
        for i in asteroids:
            while input_stack and 0 < input_stack[-1] < -i:
                input_stack.pop()
            if input_stack and i < 0 and input_stack[-1] == -i:
                input_stack.pop()
            elif i > 0 or not input_stack or input_stack[-1] < -i:
                input_stack.append(i)
        return input_stack


s = Solution()
print(s.asteroidCollision([10, 2, -5]))
