"""
Given an array nums of n integers, return an array of all the
unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
    - 0 <= a, b, c, d < n
    - a, b, c, and d are distinct.
    - nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:
    * 1 <= nums.length <= 200
    * -10^9 <= nums[i] <= 10^9
    * -10^9 <= target <= 10^9
"""

import sys

sys.path.insert(1, "../")
from utils import dtypes
from utils import run_tests

ReturnType = dtypes.List[dtypes.List[int]]


# ------------------------------SOLUTION------------------------------
def four_sum(nums: dtypes.List[int], target: int) -> ReturnType:
    nums.sort()
    ans: ReturnType = []
    seen: dtypes.Set[int] = set()

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            left: int = j + 1
            right: int = len(nums) - 1

            while left < right:
                candidates: dtypes.Set[int] = (
                    nums[i], nums[j], nums[left], nums[right]
                )

                if sum(candidates) > target:
                    right -= 1
                    continue
                elif sum(candidates) < target:
                    left += 1
                    continue
                elif sum(candidates) == target and candidates not in seen:
                    ans.append(list(candidates))
                    seen.add(candidates)

                left += 1
                right -= 1

    return ans


if __name__ == "__main__":
    test1_ans = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    run_tests.check(four_sum, test1_ans, **{"nums": [1, 0, -1, 0, -2, 2], "target": 0})

    test2_ans = [[2,2,2,2]]
    run_tests.check(four_sum, test2_ans, **{"nums": [2, 2, 2, 2, 2], "target": 8})