"""
Given an array `nums` of distinct integers, return all 
the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Constraints:
    * 1 <= nums.length <= 6
    * -10 <= nums[i] <= 10
    * All the integers of `nums` are unique.
"""

import sys

sys.path.insert(1, "../")
from utils import dtypes
from utils import run_tests

ReturnType = dtypes.List[dtypes.List[int]]


# ------------------------------SOLUTION------------------------------
def permute(nums: dtypes.List[int]) -> ReturnType:
    ans: ReturnType = []

    if len(nums) == 1: return [nums[:]]

    for _ in range(len(nums)):
        dropped_num: int = nums.pop(0)
        perms_without_dropped_num = permute(nums)

        for perm in perms_without_dropped_num: perm.append(dropped_num)

        ans.extend(perms_without_dropped_num)
        nums.append(dropped_num)

    return ans


if __name__ == "__main__":
    test1_ans = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    run_tests.check_print(permute, test1_ans, **{"nums": [1, 2, 3]})

    test2_ans = [[0, 1], [1, 0]]
    run_tests.check_print(permute, test2_ans, **{"nums": [0, 1]})
