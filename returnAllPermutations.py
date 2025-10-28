from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []
        n = len(nums)

        def backtrack(start: int) -> None:
            if start == n:
                # append a snapshot/copy of the current permutation
                res.append(nums[:])
                return
            for i in range(start, n):
                # swap current index with the loop index
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                # backtrack / undo swap
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return res
