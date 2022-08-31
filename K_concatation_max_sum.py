from typing import List


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        sum = 0
        flag = True
        for single in arr:
            if single < 0:
                flag = False
                continue
            sum += single
        if flag:
            sum *= k
        return sum % (10e9 + 7)