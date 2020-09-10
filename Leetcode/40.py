from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        def backtrack(i, tmp_sum, tmp):
            if  tmp_sum > target or i == n:
                return 
            if tmp_sum == target:
                res.append(tmp)
                return
            for j in range(i+1, n):
                if tmp_sum + candidates[j] > target:
                    break
                if j > i + 1 and candidates[j] == candidates[j-1]:
                    continue
                backtrack(j,tmp_sum + candidates[j],tmp+[candidates[j]])
        backtrack(-1, 0, [])
        return res

if __name__ == "__main__":
    print(Solution().combinationSum2([3,1,3,5,1,1],8))
