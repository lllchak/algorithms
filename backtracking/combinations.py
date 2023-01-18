"""
Given two integers n and k, return all possible 
combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

Example 2:
Input: n = 1, k = 1
Output: [[1]]

Constraints:
    * 1 <= n <= 20
    * 1 <= k <= n
"""

import sys

sys.path.insert(1, "../")
from utils import dtypes
from utils import run_tests

ReturnType = dtypes.List[dtypes.List[int]]


# ------------------------------SOLUTION------------------------------
class Solution:
    def backtrack(
        self, 
        start: int,
        ans: dtypes.List[int],
        comb: dtypes.List[int],
        n: int,
        k: int
    ) -> None:
        if len(comb) == k: 
            ans.append(comb[:])
            return
        
        for i in range(start, n + 1):
            comb.append(i)
            self.backtrack(i + 1, ans, comb, n, k)
            comb.pop()
    
    def combinations(self, n: int, k: int) -> ReturnType:
        ans: ReturnType = []
        self.backtrack(1, ans, [], n, k)

        return ans


if __name__ == "__main__":
    sol = Solution()
    test1_ans = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    run_tests.check_print(sol.combinations, test1_ans, **{"n": 4, "k": 2})

    test2_ans = [[1]]
    run_tests.check_print(sol.combinations, test2_ans, **{"n": 1, "k": 1})

