from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        length = len(cardPoints)
        if k == length:
            return sum(cardPoints)
        right_side = cardPoints.copy()
        for i in range(1, length):
            right_side[length - i - 1] += right_side[length - i]
            cardPoints[i] += cardPoints[i-1]
        max_score = max(cardPoints[k - 1], right_side[length - k])
        for i in range(k - 1):
            max_score = max(max_score, cardPoints[i] + right_side[length + i - k + 1])
        return max_score