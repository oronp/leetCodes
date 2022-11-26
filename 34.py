from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        mid = 0
        outcome = [-1, -1]
        while start <= end:
            mid = (end + start) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                outcome = firstNlast(nums, target, mid)
                return outcome
        return outcome


def firstNlast(nums, target, index):
    first = 0
    last = 0
    tmp = index
    while nums[tmp] == target and tmp > 0:
        first = tmp
        tmp -= 1
    while index < len(nums) and nums[index] == target:
        last = index
        index += 1
    return [first, last]

test_case = [5,7,7,8,8,10]
solution = Solution
print(solution.searchRange(solution, test_case, 8))