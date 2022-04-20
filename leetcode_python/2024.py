class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        return max(self.maxConsecutiveChar(answerKey, 'T', k), self.maxConsecutiveChar(answerKey, 'F', k))

    def maxConsecutiveChar(self, answerKey, ch, k):
        ch_sum, left, result = 0, 0, 0
        for i in range(len(answerKey)):
            ch_sum += answerKey[i] != ch
            while ch_sum > k:
                ch_sum -= answerKey[left] != ch
                left += 1
            result = max(result, i - left + 1)
        return result


s = Solution()
print(s.maxConsecutiveAnswers(answerKey="TTFF", k=2))
