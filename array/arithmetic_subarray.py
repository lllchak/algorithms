"""
A sequence of numbers is called arithmetic if it consists of 
at least two elements, and the difference between every 
two consecutive elements is the same. More formally, a 
sequence s is arithmetic if and only if `s[i+1] - s[i] == s[1] - s[0]`
for all valid i.

For example, these are arithmetic sequences:
    1, 3, 5, 7, 9
    7, 7, 7, 7
    3, -1, -5, -9
The following sequence is not arithmetic:
    1, 1, 2, 5, 7

You are given an array of n integers, nums, and two arrays of 
m integers each, l and r, representing the m range queries, 
where the ith query is the range [l[i], r[i]]. All the arrays are 0-indexed.

Return a list of boolean elements answer, where answer[i] is 
true if the subarray nums[l[i]], nums[l[i]+1], ... , nums[r[i]] 
can be rearranged to form an arithmetic sequence, and false otherwise.

Example 1:
Input: 
    nums = [4,6,5,9,3,7]
    l = [0,0,2]
    r = [2,3,5]
Output: [true,false,true]

Example 2:
Input: 
    nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
    l = [0,1,6,4,8,7]
    r = [4,4,9,7,9,10]
Output: [false,true,false,false,true,true]

Constraints:
    * n == nums.length
    * m == l.length
    * m == r.length
    * 2 <= n <= 500
    * 1 <= m <= 500
    * 0 <= l[i] < r[i] < n
    * -10^5 <= nums[i] <= 10^5
"""

import sys

sys.path.insert(1, "../")
from utils import dtypes
from utils import run_tests

ReturnType = dtypes.List[bool]


class Solution:
    def check(self, nums: dtypes.List[int]) -> bool:
        for i in range(len(nums) - 2):
            if nums[i + 1] - nums[i] != nums[i + 2] - nums[i + 1]: return False
        
        return True

    def check_arrays(
        self,
        nums: dtypes.List[int],
        l: dtypes.List[int],
        r: dtypes.List[int]
    ) -> ReturnType:
        ans: ReturnType = []

        for left, right in zip(l, r):
            ans.append(self.check(sorted(nums[left:right+1])))

        return ans


if __name__ == "__main__":
    sol = Solution()
    test1_ans = [True, False, True]
    assert run_tests.check_eq(sol.check_arrays, test1_ans, **{
            "nums": [4, 6, 5, 9, 3, 7],
            "l": [0, 0, 2],
            "r": [2, 3, 5]
        }
    )

    test2_ans = [False, True, False, False, True, True]
    assert run_tests.check_eq(sol.check_arrays, test2_ans, **{
            "nums": [-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10],
            "l": [0, 1, 6, 4, 8, 7],
            "r": [4, 4, 9, 7, 9, 10]
        }
    )

    print("SUCCESS")